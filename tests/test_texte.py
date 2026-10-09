from fastapi.testclient import TestClient
from app.main import app
from app.outils.texte import palindrome

client = TestClient(app)

#Test pour definir si le palindrome est: Normal, limite ou non symetrique
def test_palindrome_normal():
    assert palindrome("kayak") is True


def test_palindrome_limite():
    # Cas limite : un seul caractere
    assert palindrome("a") is True


def test_palindrome_erreur():
    # Chaine non symetrique
    assert palindrome("bonjour") is False

#Test Clients: Valide, non palindrome, invalide. 

def test_route_palindrome_valide():
    reponse = client.get("/palindrome/radar")
    assert reponse.status_code == 200
    assert reponse.json()["est_palindrome"] is True


def test_route_palindrome_non_palindrome():
    reponse = client.get("/palindrome/python")
    assert reponse.status_code == 200
    assert reponse.json()["est_palindrome"] is False


def test_route_palindrome_invalide():
    # Saisie non alphabétique -> erreur HTTP 400
    reponse = client.get("/palindrome/12345")
    assert reponse.status_code == 400