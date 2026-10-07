import pytest

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
