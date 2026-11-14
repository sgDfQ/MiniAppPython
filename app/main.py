from fastapi import FastAPI, HTTPException

from app.erreurs import erreur_400
from app.outils.conversion import celsius_fahrenheit, euros_devise, km_miles
from app.outils.math import factorielle
from app.outils.texte import compter_voyelles, inverser, palindrome
from app.outils.validation import email_valide, mdp_robuste

app = FastAPI(title="Mini API")


@app.get("/sante")
def sante():
    return {"statut": "ok"}


@app.get("/palindrome/{chaine}")
def route_palindrome(chaine: str):
    if not chaine or not chaine.isalpha():
        raise HTTPException(
            status_code=400,
            detail="Le paramètre 'chaine' est invalide : seules les lettres sont autorisées."
        )

    return {
        "chaine": chaine,
        "est_palindrome": palindrome(chaine)
    }


@app.get("/voyelles/{chaine}")
def route_voyelles(chaine: str):
    if not any(caractere.isalpha() for caractere in chaine):
        raise erreur_400("La chaîne doit contenir au moins une lettre")
    return {"chaine": chaine, "nombre_voyelles": compter_voyelles(chaine)}


@app.get("/inverser/{chaine}")
def route_inverser(chaine: str):
    a_lettre = any(caractere.isalpha() for caractere in chaine)
    a_chiffre = any(caractere.isdigit() for caractere in chaine)
    if not a_lettre or a_chiffre:
        raise erreur_400("La chaîne doit contenir du texte, sans chiffres")
    return {"chaine": chaine, "inverse": inverser(chaine)}


@app.get("/email-valide/{email}")
def route_email_valide(email: str):
    if not email_valide(email):
        raise erreur_400("Email invalide")
    return {"email": email, "valide": True}


@app.get("/mdp-robuste/{mdp}")
def route_mdp_robuste(mdp: str):
    if not mdp_robuste(mdp):
        raise erreur_400("Mot de passe trop faible : 8 caractères minimum, avec majuscule, minuscule et chiffre")
    return {"valide": True}


@app.get("/factorielle/{n}")
def route_factorielle(n: int):
    try:
        return {"n": n, "resultat": factorielle(n)}
    except ValueError as e:
        raise erreur_400(str(e))


@app.get("/celsius-fahrenheit/{c}")
def route_celsius_fahrenheit(c: float):
    try:
        return {"c": c, "resultat": celsius_fahrenheit(c)}
    except ValueError as e:
        raise erreur_400(str(e))


@app.get("/km-miles/{km}")
def route_km_miles(km: float):
    try:
        return {"km": km, "resultat": km_miles(km)}
    except ValueError as e:
        raise erreur_400(str(e))


@app.get("/euros-devise/{montant}/{devise}")
def route_euros_devise(montant: float, devise: str):
    try:
        return {"montant": montant, "devise": devise.upper(),
                "resultat": euros_devise(montant, devise)}
    except ValueError as e:
        raise erreur_400(str(e))