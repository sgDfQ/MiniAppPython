import math
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/math/factorielle")
def factorielle(n: int):
    if n < 0:
        raise HTTPException(status_code=400, detail="Le nombre doit être positif ou nul.")
    return {"resultat": math.factorial(n)}

@app.get("/math/est_premier")
def est_premier(n: int):
    if n < 0:
        raise HTTPException(status_code=400, detail="Le nombre doit être positif.")
    if n < 2:
        return {"resultat": False}
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return {"resultat": False}
    return {"resultat": True}

@app.get("/math/pgcd")
def pgcd(a: int, b: int):
    if a < 0 or b < 0:
        raise HTTPException(status_code=400, detail="Les nombres doivent être positifs.")
    return {"resultat": math.gcd(a, b)}