"""
Unit tests for app.py
This is exactly what GitHub Actions will run automatically on every push.
"""

from app import app, add


def test_add():
    assert add(2, 3) == 5


def test_home_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data


def test_health_route():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"
