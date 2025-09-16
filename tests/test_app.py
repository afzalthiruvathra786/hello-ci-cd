from src.app import app

def test_root():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hello, CI/CD!" in resp.data

