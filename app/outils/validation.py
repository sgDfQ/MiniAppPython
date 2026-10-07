import re


def email_valide(email):
    motif = r"[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}"
    resultat = re.fullmatch(motif, email)
    return resultat is not None