ZERO_ABSOLU = -273.15




def celsius_fahrenheit(c: float) -> float:
    """Convertit des degrés Celsius en degrés Fahrenheit."""
    if c < ZERO_ABSOLU:
        raise ValueError("température sous le zéro absolu (-273.15 °C)")
    return c * 1.8 + 32

