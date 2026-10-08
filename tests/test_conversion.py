import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.outils.conversion import celsius_fahrenheit, euros_devise, km_miles

# --- celsius_fahrenheit ---

def test_celsius_fahrenheit_de_100():
    assert celsius_fahrenheit(100) == 212


def test_celsius_fahrenheit_de_moins_40():
    assert celsius_fahrenheit(-40) == -40


def test_celsius_fahrenheit_sous_zero_absolu():
    with pytest.raises(ValueError):
        celsius_fahrenheit(-300)


# --- km_miles ---

def test_km_miles_de_10():
    assert round(km_miles(10), 2) == 6.21


def test_km_miles_de_0():
    assert km_miles(0) == 0


def test_km_miles_negatif():
    with pytest.raises(ValueError):
        km_miles(-5)


        # --- euros_devise ---

def test_euros_devise_100_en_usd():
    assert euros_devise(100, "USD") == 108


def test_euros_devise_de_0():
    assert euros_devise(0, "GBP") == 0


def test_euros_devise_negatif():
    with pytest.raises(ValueError):
        euros_devise(-10, "USD")


def test_euros_devise_inconnue():
    with pytest.raises(ValueError):
        euros_devise(100, "XYZ")


client = TestClient(app)


def test_route_celsius_fahrenheit_ok():
    r = client.get("/celsius-fahrenheit/100")
    assert r.status_code == 200
    assert r.json()["resultat"] == 212


def test_route_celsius_fahrenheit_400():
    r = client.get("/celsius-fahrenheit/-300")
    assert r.status_code == 400


def test_route_km_miles_400():
    r = client.get("/km-miles/-5")
    assert r.status_code == 400


def test_route_euros_devise_400():
    r = client.get("/euros-devise/100/XYZ")
    assert r.status_code == 400
