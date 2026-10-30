import math

ZERO_ABSOLU = -273.15
KM_PAR_MILE = 1.609344
TAUX_EUR = {"USD": 1.08, "GBP": 0.85, "JPY": 160.0, "CHF": 0.94}


def _verifier_fini(valeur: float) -> None:
    """Refuse NaN et l'infini, qui ne peuvent pas être renvoyés en JSON."""
    if not math.isfinite(valeur):
        raise ValueError("la valeur doit être un nombre fini")


def celsius_fahrenheit(c: float) -> float:
    """Convertit des degrés Celsius en degrés Fahrenheit."""
    _verifier_fini(c)
    if c < ZERO_ABSOLU:
        raise ValueError("température sous le zéro absolu (-273.15 °C)")
    resultat = c * 1.8 + 32
    _verifier_fini(resultat)
    return resultat


def km_miles(km: float) -> float:
    """Convertit des kilomètres en miles terrestres."""
    _verifier_fini(km)
    if km < 0:
        raise ValueError("une distance ne peut pas être négative")
    return km / KM_PAR_MILE


def euros_devise(montant: float, devise: str) -> float:
    """Convertit un montant en euros vers une devise, avec des taux fixes."""
    _verifier_fini(montant)
    if montant < 0:
        raise ValueError("le montant ne peut pas être négatif")
    devise = devise.strip().upper()
    if devise not in TAUX_EUR:
        raise ValueError(f"devise inconnue : {devise}")
    resultat = round(montant * TAUX_EUR[devise], 2)
    _verifier_fini(resultat)
    return resultat