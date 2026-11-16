import math

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.outils.math import (
    EST_PREMIER_MAX,
    FACTORIELLE_MAX,
    est_premier,
    factorielle,
    pgcd,
)

client = TestClient(app)


# --- factorielle : fonction ---

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


# --- factorielle : route ---

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


# --- est_premier : fonction ---

def test_est_premier_cas_normal():
    assert est_premier(7) is True
    assert est_premier(9) is False


def test_est_premier_cas_limite():
    assert est_premier(0) is False
    assert est_premier(1) is False
    assert est_premier(2) is True


def test_est_premier_negatif_leve_erreur():
    with pytest.raises(ValueError):
        est_premier(-1)


def test_est_premier_trop_grand_leve_erreur():
    with pytest.raises(ValueError):
        est_premier(EST_PREMIER_MAX + 1)


# --- est_premier : route ---

def test_route_est_premier_cas_normal():
    reponse = client.get("/est-premier/7")
    assert reponse.status_code == 200
    assert reponse.json() == {"n": 7, "est_premier": True}


def test_route_est_premier_cas_erreur():
    reponse = client.get("/est-premier/-3")
    assert reponse.status_code == 400
    assert reponse.json()["detail"] == "Le nombre doit être positif ou nul."


# --- pgcd : fonction ---

def test_pgcd_cas_normal():
    assert pgcd(12, 18) == 6
    assert pgcd(7, 13) == 1


def test_pgcd_cas_limite():
    assert pgcd(0, 5) == 5
    assert pgcd(-12, 18) == 6


def test_pgcd_zero_zero_leve_erreur():
    with pytest.raises(ValueError):
        pgcd(0, 0)


# --- pgcd : route ---

def test_route_pgcd_cas_normal():
    reponse = client.get("/pgcd/12/18")
    assert reponse.status_code == 200
    assert reponse.json() == {"a": 12, "b": 18, "resultat": 6}


def test_route_pgcd_cas_erreur():
    reponse = client.get("/pgcd/0/0")
    assert reponse.status_code == 400
    assert reponse.json()["detail"] == "Le PGCD de 0 et 0 n'est pas défini."