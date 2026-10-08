from fastapi import FastAPI

from app.erreurs import erreur_400
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
