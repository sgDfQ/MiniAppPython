import unicodedata


def palindrome(chaine: str) -> bool:
    """Ignore la casse, les accents, les espaces et la ponctuation."""
    sans_accents = unicodedata.normalize("NFD", chaine)
    lettres = [c.lower() for c in sans_accents if c.isalnum()]
    return lettres == lettres[::-1]
