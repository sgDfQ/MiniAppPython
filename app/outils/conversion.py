ZERO_ABSOLU = -273.15




def celsius_fahrenheit(c: float) -> float:
    """Convertit des degrés Celsius en degrés Fahrenheit."""
    if c < ZERO_ABSOLU:
        raise ValueError("température sous le zéro absolu (-273.15 °C)")
    return c * 1.8 + 32

KM_PAR_MILE = 1.609344
def km_miles(km: float) -> float:
    """Convertit des kilomètres en miles terrestres."""
    if km < 0:
        raise ValueError("une distance ne peut pas être négative")
    return km / KM_PAR_MILE 

TAUX_EUR = {"USD": 1.08, "GBP": 0.85, "JPY": 160.0, "CHF": 0.94}
def euros_devise(montant: float, devise: str) -> float:
    """Convertit un montant en euros vers une devise, avec des taux fixes."""
    if montant < 0:
        raise ValueError("le montant ne peut pas être négatif")
    devise = devise.strip().upper()
    if devise not in TAUX_EUR:
        raise ValueError(f"devise inconnue : {devise}")
    return round(montant * TAUX_EUR[devise], 2)