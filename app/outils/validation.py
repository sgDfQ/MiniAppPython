import re

# Pas de points consécutifs, ni en début ou fin de partie, extension de 2 lettres minimum
MOTIF_EMAIL = r"[^@\s.]+(\.[^@\s.]+)*@[^@\s.]+(\.[^@\s.]+)*\.[a-zA-Z]{2,}"


def email_valide(email: str) -> bool:
    return re.fullmatch(MOTIF_EMAIL, email) is not None


def mdp_robuste(mdp: str) -> bool:
    a_majuscule = any(c.isupper() for c in mdp)
    a_minuscule = any(c.islower() for c in mdp)
    a_chiffre = any(c in "0123456789" for c in mdp)
    return len(mdp) >= 8 and a_majuscule and a_minuscule and a_chiffre
