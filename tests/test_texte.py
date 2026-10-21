from fastapi.testclient import TestClient

from app.main import app
from app.outils.texte import palindrome

client = TestClient(app)


# Fonction palindrome : cas normal, limites, erreur
def test_palindrome_normal():
    assert palindrome("kayak") is True


def test_palindrome_limite():
    assert palindrome("a") is True


def test_palindrome_majuscules_accents():
    assert palindrome("Ésé") is True


def test_palindrome_phrase():
    assert palindrome("Esope reste ici et se repose") is True


def test_palindrome_erreur():
    assert palindrome("bonjour") is False


# Route /palindrome : valide, non palindrome, invalide
def test_route_palindrome_valide():
    reponse = client.get("/palindrome/radar")
    assert reponse.status_code == 200
    assert reponse.json()["est_palindrome"] is True


def test_route_palindrome_phrase():
    reponse = client.get("/palindrome/Esope reste ici et se repose")
    assert reponse.status_code == 200
    assert reponse.json()["est_palindrome"] is True


def test_route_palindrome_non_palindrome():
    reponse = client.get("/palindrome/python")
    assert reponse.status_code == 200
    assert reponse.json()["est_palindrome"] is False


def test_route_palindrome_invalide():
    reponse = client.get("/palindrome/12345")
    assert reponse.status_code == 400
