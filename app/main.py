from fastapi import FastAPI

from app.erreurs import erreur_400
from app.outils.conversion import celsius_fahrenheit, euros_devise, km_miles
from app.outils.validation import email_valide

app = FastAPI(title="Mini API")



@app.get("/sante")
def sante():
    return {"statut": "ok"}


@app.get("/email-valide/{email}")
def route_email_valide(email: str):
    if email.strip() == "":
        raise erreur_400("L'email ne doit pas être vide")
    return {"email": email, "valide": email_valide(email)}

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
    