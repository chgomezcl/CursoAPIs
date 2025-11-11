# Prueba básica de listado de usuarios
from fastapi.testclient import TestClient
from app.main import app
 
client = TestClient(app)
 
def test_get_users():
    res = client.get("/users/")
    assert res.status_code == 200