from fastapi import HTTPException


def erreur_400(message: str) -> HTTPException:
    """Construit l'erreur HTTP 400 utilisée par toutes les routes."""
    return HTTPException(status_code=400, detail=message)
