#import pytest


def always_returns_true():
    return False

def merge_conflict_function():
    pass

def test_always_returns_true():
    assert always_returns_true()

def adriana_says_hello_world():
    user_input = None
    user_name = input("What is your name? ")
    while user_input != ("hello" or "Hello"):
        user_input = input("Say hello to Adriana! (You must only type hello): ")
    print(f"Hello, {user_name}! You're so kind to say hello. Hello!")

def merge_conflict_function():
    print("hi")

adriana_says_hello_world()
