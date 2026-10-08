import re


def email_valide(email):
    motif = r"[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}"
    resultat = re.fullmatch(motif, email)
    return resultat is not None

def mdp_robuste(mdp):
    a_majuscule = False
    a_minuscule = False
    a_chiffre = False

    for caractere in mdp:
        if caractere.isupper():
            a_majuscule = True
        if caractere.islower():
            a_minuscule = True
        if caractere.isdigit():
            a_chiffre = True

    return len(mdp) >= 8 and a_majuscule and a_minuscule and a_chiffre