from fastapi import FastAPI

from app.erreurs import erreur_400
from app.outils.validation import email_valide, mdp_robuste

app = FastAPI(title="Mini API")



@app.get("/sante")
def sante():
    return {"statut": "ok"}


@app.get("/email-valide/{email}")
def route_email_valide(email: str):
    if email.strip() == "":
        raise erreur_400("L'email ne doit pas être vide")
    return {"email": email, "valide": email_valide(email)}

@app.get("/mdp-robuste/{mdp}")
def route_mdp_robuste(mdp: str):
    if not mdp_robuste(mdp):
        raise erreur_400("Mot de passe trop faible : 8 caractères minimum, avec majuscule, minuscule et chiffre")
    return {"valide": True}