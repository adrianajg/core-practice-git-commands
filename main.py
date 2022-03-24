import pytest


def always_returns_true():
    return False

def merge_conflict_function():
    pass

def test_always_returns_true():
    assert always_returns_true()
