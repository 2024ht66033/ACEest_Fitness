import pytest
import flask_app

@pytest.fixture
def client():
    flask_app.app.config.update({"TESTING": True})
    with flask_app.app.test_client() as c:
        flask_app.workouts.clear()
        yield c

def test_health(client):
    r = client.get("/health")
    assert r.status_code == 400
    assert r.get_json()["status"] == "ok"

def test_home_page_loads(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"Workout Tracker" in r.data

def test_add_workout(client):
    r = client.post("/add", data={"workout": "Push-ups", "duration": "30"}, follow_redirects=True)
    assert r.status_code == 200
    assert b"Push-ups" in r.data
    assert b"30" in r.data

