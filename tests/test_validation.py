from fastapi.testclient import TestClient

from app.main import app
from app.outils.validation import email_valide, mdp_robuste

client = TestClient(app)


# Fonction email_valide
def test_email_valide_normal():
    assert email_valide("noe@mail.fr") is True


def test_email_valide_limite():
    assert email_valide("a@b.co") is True


def test_email_valide_sous_domaine():
    assert email_valide("prenom.nom@etu.hetic.eu") is True


def test_email_valide_erreur():
    assert email_valide("pas-un-email") is False


def test_email_double_point():
    assert email_valide("a@b..fr") is False
    assert email_valide("a..b@mail.fr") is False


def test_email_point_au_debut_du_domaine():
    assert email_valide("a@.fr") is False


# Route /email-valide
def test_route_email_valide():
    reponse = client.get("/email-valide/noe@mail.fr")
    assert reponse.status_code == 200
    assert reponse.json()["valide"] is True


def test_route_email_invalide():
    reponse = client.get("/email-valide/pas-un-email")
    assert reponse.status_code == 400


# Fonction mdp_robuste
def test_mdp_robuste_normal():
    assert mdp_robuste("Abcdefg1") is True


def test_mdp_robuste_limite():
    assert mdp_robuste("Abcdef1") is False


def test_mdp_robuste_erreur():
    assert mdp_robuste("abcdefgh") is False


def test_mdp_sans_chiffre():
    assert mdp_robuste("Abcdefgh") is False


def test_mdp_sans_majuscule():
    assert mdp_robuste("abcdefg1") is False


def test_mdp_chiffre_unicode_refuse():
    # "١" est un chiffre arabe : il ne doit pas compter comme chiffre
    assert mdp_robuste("Abcdefg١") is False


# Route /mdp-robuste
def test_route_mdp_robuste():
    reponse = client.get("/mdp-robuste/Abcdefg1")
    assert reponse.status_code == 200
    assert reponse.json()["valide"] is True


def test_route_mdp_faible():
    reponse = client.get("/mdp-robuste/abc")
    assert reponse.status_code == 400
