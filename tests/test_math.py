import math

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.outils.math import FACTORIELLE_MAX, factorielle

client = TestClient(app)


# --- Tests unitaires : fonction factorielle ---

def test_factorielle_cas_normal():
    assert factorielle(5) == 120


def test_factorielle_cas_limite():
    assert factorielle(0) == 1


def test_factorielle_valeur_max_autorisee():
    assert factorielle(FACTORIELLE_MAX) == math.factorial(FACTORIELLE_MAX)


def test_factorielle_negatif_leve_erreur():
    with pytest.raises(ValueError):
        factorielle(-1)


def test_factorielle_trop_grand_leve_erreur():
    with pytest.raises(ValueError):
        factorielle(FACTORIELLE_MAX + 1)


# --- Tests d'intégration : route /factorielle/{n} ---

def test_route_factorielle_cas_normal():
    reponse = client.get("/factorielle/5")
    assert reponse.status_code == 200
    assert reponse.json() == {"n": 5, "resultat": 120}


def test_route_factorielle_cas_erreur():
    reponse = client.get("/factorielle/-1")
    assert reponse.status_code == 400
    assert reponse.json()["detail"] == "Le nombre doit être positif ou nul."


def test_route_factorielle_grande_valeur_renvoie_400():
    reponse = client.get("/factorielle/5000")
    assert reponse.status_code == 400