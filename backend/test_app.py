from app import app

def test_health():
    client = app.test_client()
    res = client.get("/health")
    assert res.status_code == 200

def test_message():
    client = app.test_client()
    res = client.get("/api/message")
    assert res.status_code == 200
    assert b"Hello" in res.data

