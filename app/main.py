from fastapi import FastAPI

from app.erreurs import erreur_400
from app.outils.math import factorielle

app = FastAPI(title="Mini API")


@app.get("/sante")
def sante():
    return {"statut": "ok"}


@app.get("/factorielle/{n}")
def route_factorielle(n: int):
    try:
        return {"n": n, "resultat": factorielle(n)}
    except ValueError as e:
        raise erreur_400(str(e))
