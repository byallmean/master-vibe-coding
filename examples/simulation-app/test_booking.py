"""Unit tests for booking overlap logic."""
import unittest
from booking import can_book


class TestBooking(unittest.TestCase):
    def test_no_overlap(self):
        self.assertTrue(can_book([(9, 10)], 10, 11))

    def test_overlap(self):
        self.assertFalse(can_book([(9, 10)], 9, 10))

    def test_partial_overlap(self):
        self.assertFalse(can_book([(9, 11)], 10, 12))

    def test_invalid_range(self):
        self.assertFalse(can_book([], 11, 11))

    def test_empty_calendar(self):
        self.assertTrue(can_book([], 9, 10))


if __name__ == "__main__":
    unittest.main()
