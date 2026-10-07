from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_route_factorielle_cas_normal():
    reponse = client.get("/factorielle/5")
    assert reponse.status_code == 200
    assert reponse.json() == {"n": 5, "resultat": 120}


def test_route_factorielle_cas_erreur():
    reponse = client.get("/factorielle/-1")
    assert reponse.status_code == 400
    assert reponse.json()["detail"] == "Le nombre doit être positif ou nul."
