from app.main import app, tasks


def client():
    return app.test_client()


def test_health():
    r = client().get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_add_and_list_task():
    tasks.clear()
    c = client()
    r = c.post("/tasks", json={"title": "Learn DevOps"})
    assert r.status_code == 201
    r = c.get("/tasks")
    assert len(r.get_json()) == 1


def test_add_task_without_title():
    r = client().post("/tasks", json={})
    assert r.status_code == 400