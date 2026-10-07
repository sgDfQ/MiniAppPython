from fastapi.testclient import TestClient

from app.main import app
from app.outils.validation import email_valide


def test_email_valide_normal():
    assert email_valide("noe@mail.fr") is True


def test_email_valide_limite():
    assert email_valide("a@b.co") is True


def test_email_valide_erreur():
    assert email_valide("pas-un-email") is False


client = TestClient(app)


def test_route_email_valide():
    reponse = client.get("/email-valide/noe@mail.fr")
    assert reponse.status_code == 200
    assert reponse.json()["valide"] is True


def test_route_email_invalide():
    reponse = client.get("/email-valide/pas-un-email")
    assert reponse.status_code == 200
    assert reponse.json()["valide"] is False