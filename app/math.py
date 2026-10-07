import math
from fastapi import HTTPException
def factorielle(n: int):
    if n < 0:
        raise HTTPException(status_code=400, detail="Le nombre doit être positif ou nul.")
    return {"resultat": math.factorial(n)}
