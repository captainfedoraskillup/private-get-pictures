from backend import app
import requests


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200


def test_pictures_check_content_type_equals_json(client):
    res = client.get("/pictures")
    assert res.headers["Content-Type"] == "application/json"


def test_pictures_json_is_not_empty(client):
    res = client.get("/pictures")
    assert len(res.json) > 0


def test_pictures_json_is_10(client):
    res = client.get("/pictures")
    assert len(res.json) == 10
