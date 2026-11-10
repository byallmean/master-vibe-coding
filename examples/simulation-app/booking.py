"""Simple booking overlap logic for the simulation example."""


def overlaps(start_a, end_a, start_b, end_b):
    return start_a < end_b and start_b < end_a


def can_book(existing, start, end):
    if start >= end:
        return False
    for item in existing:
        if overlaps(start, end, item[0], item[1]):
            return False
    return True
