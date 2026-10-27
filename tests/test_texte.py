from fastapi.testclient import TestClient

from app.main import app
from app.outils.texte import compter_voyelles, inverser, palindrome

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


#Test pour compter les voyelles: Normal, majuscules, accents, sans voyelle
def test_compter_voyelles_normal():
    assert compter_voyelles("bonjour") == 3


def test_compter_voyelles_majuscules():
    assert compter_voyelles("AEIOU") == 5


def test_compter_voyelles_accents():
    assert compter_voyelles("été") == 2


def test_compter_voyelles_limite():
    # Cas limite : aucune voyelle
    assert compter_voyelles("bcdfg") == 0

#Test Clients: Valide, sans voyelle, invalide.

def test_route_voyelles_valide():
    reponse = client.get("/voyelles/bonjour")
    assert reponse.status_code == 200
    assert reponse.json()["nombre_voyelles"] == 3


def test_route_voyelles_sans_voyelle():
    reponse = client.get("/voyelles/bcdfg")
    assert reponse.status_code == 200
    assert reponse.json()["nombre_voyelles"] == 0


def test_route_voyelles_invalide():
    # Saisie sans lettre -> erreur HTTP 400
    reponse = client.get("/voyelles/12345")
    assert reponse.status_code == 400


#Test pour inverser le texte: Normal, majuscules et accents, limite
def test_inverser_normal():
    assert inverser("bonjour") == "ruojnob"


def test_inverser_majuscules_accents():
    assert inverser("Élan") == "nalÉ"


def test_inverser_limite():
    # Cas limite : un seul caractere
    assert inverser("a") == "a"

#Test Clients: Valide, avec espaces, chiffres seuls, texte avec chiffres.

def test_route_inverser_valide():
    reponse = client.get("/inverser/bonjour")
    assert reponse.status_code == 200
    assert reponse.json()["inverse"] == "ruojnob"


def test_route_inverser_espaces():
    reponse = client.get("/inverser/bonjour le monde")
    assert reponse.status_code == 200
    assert reponse.json()["inverse"] == "ednom el ruojnob"


def test_route_inverser_invalide():
    # Saisie de chiffres -> erreur HTTP 400
    reponse = client.get("/inverser/12345")
    assert reponse.status_code == 400


def test_route_inverser_texte_avec_chiffres():
    # Texte melange avec des chiffres -> erreur HTTP 400
    reponse = client.get("/inverser/abc1")
    assert reponse.status_code == 400
