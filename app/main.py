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

