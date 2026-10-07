from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# --- Tests Factorielle ---
def test_factorielle_normal():
    response = client.get("/math/factorielle?n=5")
    assert response.status_code == 200
    assert response.json() == {"resultat": 120}

def test_factorielle_limite():
    response = client.get("/math/factorielle?n=0")
    assert response.status_code == 200
    assert response.json() == {"resultat": 1}

def test_factorielle_erreur():
    response = client.get("/math/factorielle?n=-5")
    assert response.status_code == 400

# --- Tests Est Premier ---
def test_est_premier_normal():
    response = client.get("/math/est_premier?n=7")
    assert response.status_code == 200
    assert response.json() == {"resultat": True}

def test_est_premier_limite():
    response = client.get("/math/est_premier?n=1")
    assert response.status_code == 200
    assert response.json() == {"resultat": False}

def test_est_premier_erreur():
    response = client.get("/math/est_premier?n=-3")
    assert response.status_code == 400

# --- Tests PGCD ---
def test_pgcd_normal():
    response = client.get("/math/pgcd?a=48&b=18")
    assert response.status_code == 200
    assert response.json() == {"resultat": 6}

def test_pgcd_limite():
    response = client.get("/math/pgcd?a=0&b=5")
    assert response.status_code == 200
    assert response.json() == {"resultat": 5}

def test_pgcd_erreur():
    response = client.get("/math/pgcd?a=-4&b=10")
    assert response.status_code == 400