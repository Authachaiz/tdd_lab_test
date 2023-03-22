from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_callname_get():
    name = "Authachai"
    response = client.get(f"/callname/{name}")
    assert response.status_code == 200
    assert response.json() == {"hello": name}

def test_callname_post():
    name = "Iffan"
    response = client.post("/callname", json={"name": name})
    assert response.status_code == 200
    assert response.json() == {"hello": name}
