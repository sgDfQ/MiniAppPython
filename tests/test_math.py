import pytest

from app.outils.math import factorielle


def test_factorielle_cas_normal():
    assert factorielle(5) == 120


def test_factorielle_cas_limite():
    assert factorielle(0) == 1


def test_factorielle_cas_erreur():
    with pytest.raises(ValueError):
        factorielle(-1)
