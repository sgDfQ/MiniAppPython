from fastapi import FastAPI

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