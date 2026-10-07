from fastapi.testclient import TestClient

from app.main import app
from app.outils.validation import email_valide, mdp_robuste


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
    assert reponse.status_code == 400


def test_mdp_robuste_normal():
    assert mdp_robuste("Abcdefg1") is True


def test_mdp_robuste_limite():
    assert mdp_robuste("Abcdef1") is False


def test_mdp_robuste_erreur():
    assert mdp_robuste("abcdefgh") is False


def test_route_mdp_robuste():
    reponse = client.get("/mdp-robuste/Abcdefg1")
    assert reponse.status_code == 200
    assert reponse.json()["valide"] is True


def test_route_mdp_faible():
    reponse = client.get("/mdp-robuste/abc")
    assert reponse.status_code == 400