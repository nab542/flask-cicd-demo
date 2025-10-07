import os
import sys

# Make sure the parent directory (where app.py lives) is in Python's path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # Now this works both locally and in CI

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Hello from CI/CD!"
