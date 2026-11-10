"""Tiny JSON API in Python standard library only, no pip install.

Endpoints:
  GET  /health     - health check, no auth
  GET  /items      - list items
  POST /items      - create an item with input validation
  GET  /protected  - requires a bearer value read from the environment
  POST /login      - login-shaped endpoint with a per-IP rate limit

Skill rules demonstrated: server-side input validation, never trust the
client (extra fields in the request body are ignored, not stored),
auth secret read from the environment and never hardcoded, and a
per-IP rate limit on the login-shaped endpoint.
"""
import json
import os
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

MAX_NAME_LENGTH = 100
MAX_NOTE_LENGTH = 500
RATE_LIMIT_MAX = 5
RATE_LIMIT_WINDOW_SECONDS = 60

ALLOWED_ITEM_FIELDS = ("name", "note")


class ApiState:
    """In-memory store. One instance per server, so tests stay isolated."""

    def __init__(self, bearer):
        self.items = []
        self.next_id = 1
        self.bearer = bearer
        self.login_attempts = {}
        self.lock = threading.Lock()

    def login_allowed(self, client_ip):
        now = time.monotonic()
        with self.lock:
            attempts = [t for t in self.login_attempts.get(client_ip, [])
                       if now - t < RATE_LIMIT_WINDOW_SECONDS]
            if len(attempts) >= RATE_LIMIT_MAX:
                self.login_attempts[client_ip] = attempts
                return False
            attempts.append(now)
            self.login_attempts[client_ip] = attempts
            return True


def validate_item(body):
    """Return (problem, item) where problem is an error string or None."""
    if not isinstance(body, dict):
        return "body must be a JSON object", None
    name = body.get("name")
    if not isinstance(name, str):
        return "name must be a string", None
    name = name.strip()
    if not name:
        return "name must not be empty", None
    if len(name) > MAX_NAME_LENGTH:
        return "name must be at most 100 characters", None
    note = body.get("note", "")
    if not isinstance(note, str):
        return "note must be a string", None
    if len(note) > MAX_NOTE_LENGTH:
        return "note must be at most 500 characters", None
    # Allowlist: only name and note are ever stored. Anything else in
    # the request body (for example is_admin) is ignored, not stored.
    return None, {"name": name, "note": note}


def make_handler(state):
    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def log_message(self, *args):
            pass

        def _send_json(self, status, obj):
            body = json.dumps(obj).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _read_json_body(self):
            length = int(self.headers.get("Content-Length") or 0)
            raw = self.rfile.read(length) if length else b""
            if not raw:
                return None, "empty body"
            try:
                return json.loads(raw.decode("utf-8")), None
            except (ValueError, UnicodeDecodeError):
                return None, "body must be valid JSON"

        def _client_ip(self):
            return self.client_address[0]

        def do_GET(self):
            if self.path == "/health":
                self._send_json(200, {"ok": True})
            elif self.path == "/items":
                with state.lock:
                    items = list(state.items)
                self._send_json(200, {"items": items})
            elif self.path == "/protected":
                header = self.headers.get("Authorization") or ""
                expected = "Bearer " + state.bearer
                if not state.bearer or header != expected:
                    self._send_json(401, {"error": "unauthorized"})
                else:
                    self._send_json(200, {"ok": True, "message": "welcome"})
            else:
                self._send_json(404, {"error": "not found"})

        def do_POST(self):
            if self.path == "/items":
                body, problem = self._read_json_body()
                if problem:
                    self._send_json(400, {"error": problem})
                    return
                problem, item = validate_item(body)
                if problem:
                    self._send_json(400, {"error": problem})
                    return
                with state.lock:
                    item = {"id": state.next_id, **item}
                    state.next_id += 1
                    state.items.append(item)
                self._send_json(201, {"item": item})
            elif self.path == "/login":
                if not state.login_allowed(self._client_ip()):
                    self._send_json(429, {"error": "too many requests"})
                    return
                body, problem = self._read_json_body()
                if problem:
                    self._send_json(400, {"error": problem})
                    return
                if not isinstance(body, dict) or not str(body.get("username") or "").strip():
                    self._send_json(400, {"error": "username must not be empty"})
                    return
                self._send_json(200, {"ok": True, "message": "login attempt recorded"})
            else:
                self._send_json(404, {"error": "not found"})

    return Handler


def create_server(port=0, bearer=None):
    """Build the server. The bearer value comes from the caller or from
    the API_BEARER environment variable. It is never hardcoded here."""
    if bearer is None:
        bearer = os.environ.get("API_BEARER", "")
    state = ApiState(bearer)
    return ThreadingHTTPServer(("127.0.0.1", port), make_handler(state))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    server = create_server(port)
    print(f"API listening at http://127.0.0.1:{port}/")
    server.serve_forever()
