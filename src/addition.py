# app.py
# This is a test commit
# this is to view how github actions working
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
