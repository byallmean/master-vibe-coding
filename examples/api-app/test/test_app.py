"""Tests for the tiny JSON API. Python standard library only.
Run with: python3 -m unittest discover -s test -v
"""
import json
import os
import sys
import threading
import unittest
import urllib.error
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import create_server

BEARER = "test-bearer-value"


class ApiTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = create_server(0, bearer=BEARER)
        cls.port = cls.server.server_address[1]
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def request(self, method, path, body=None, headers=None):
        url = f"http://127.0.0.1:{self.port}{path}"
        data = json.dumps(body).encode("utf-8") if body is not None else None
        req = urllib.request.Request(url, data=data, method=method)
        if data is not None:
            req.add_header("Content-Type", "application/json")
        for key, value in (headers or {}).items():
            req.add_header(key, value)
        try:
            with urllib.request.urlopen(req) as resp:
                return resp.status, json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as err:
            return err.code, json.loads(err.read().decode("utf-8"))

    def test_health_ok(self):
        status, body = self.request("GET", "/health")
        self.assertEqual(status, 200)
        self.assertTrue(body["ok"])

    def test_create_item_and_list_it(self):
        status, body = self.request("POST", "/items", {"name": "Bút bi"})
        self.assertEqual(status, 201)
        self.assertEqual(body["item"]["name"], "Bút bi")
        self.assertIn("id", body["item"])

        status, body = self.request("GET", "/items")
        self.assertEqual(status, 200)
        names = [item["name"] for item in body["items"]]
        self.assertIn("Bút bi", names)

    def test_create_item_empty_name_rejected(self):
        status, body = self.request("POST", "/items", {"name": "   "})
        self.assertEqual(status, 400)
        self.assertIn("empty", body["error"])

    def test_create_item_missing_name_rejected(self):
        status, body = self.request("POST", "/items", {"note": "no name"})
        self.assertEqual(status, 400)

    def test_create_item_overlong_name_rejected(self):
        status, body = self.request("POST", "/items", {"name": "x" * 101})
        self.assertEqual(status, 400)
        self.assertIn("100", body["error"])

    def test_protected_without_auth_rejected(self):
        status, body = self.request("GET", "/protected")
        self.assertEqual(status, 401)
        self.assertIn("error", body)

    def test_protected_with_wrong_bearer_rejected(self):
        status, _ = self.request(
            "GET", "/protected", headers={"Authorization": "Bearer wrong-value"})
        self.assertEqual(status, 401)

    def test_protected_with_correct_bearer_ok(self):
        status, body = self.request(
            "GET", "/protected", headers={"Authorization": "Bearer " + BEARER})
        self.assertEqual(status, 200)
        self.assertTrue(body["ok"])

    def test_mass_assignment_extra_fields_ignored(self):
        status, body = self.request("POST", "/items", {
            "name": "Vở",
            "note": "kẻ ngang",
            "is_admin": True,
            "role": "admin",
            "credits": 99999,
        })
        self.assertEqual(status, 201)
        item = body["item"]
        self.assertNotIn("is_admin", item)
        self.assertNotIn("role", item)
        self.assertNotIn("credits", item)
        self.assertEqual(set(item.keys()), {"id", "name", "note"})

    def test_login_rate_limit(self):
        statuses = []
        for _ in range(6):
            status, _ = self.request("POST", "/login", {"username": "demo"})
            statuses.append(status)
        self.assertEqual(statuses[:5], [200, 200, 200, 200, 200])
        self.assertEqual(statuses[5], 429)


if __name__ == "__main__":
    unittest.main()
