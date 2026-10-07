from app.outils.validation import email_valide


def test_email_valide_normal():
    assert email_valide("noe@mail.fr") is True


def test_email_valide_limite():
    assert email_valide("a@b.co") is True


def test_email_valide_erreur():
    assert email_valide("pas-un-email") is False