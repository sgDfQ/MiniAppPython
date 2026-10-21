# MiniAppPython

#Not the final README, Only a first version (@sgDfQ)

Petite API FastAPI d'outils de texte : palindrome, validation d'email, robustesse de mot de passe.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt   # ou requirements.txt pour la prod uniquement
```

## Lancer l'API

```bash
uvicorn app.main:app --reload
```

Documentation interactive : http://127.0.0.1:8000/docs

## Routes

| Méthode | Route | Entrée | Réponse |
|---|---|---|---|
| GET | `/sante` | — | `{"statut": "ok"}` |
| GET | `/palindrome/{chaine}` | texte dans l'URL (au moins une lettre) | `{"chaine": ..., "est_palindrome": bool}` |
| GET | `/email-valide/{email}` | email dans l'URL | `{"email": ..., "valide": true}` ou 400 |
| GET | `/mdp-robuste/{mdp}` | mot de passe dans l'URL | `{"valide": true}` ou 400 |

## Tests et lint

```bash
ruff check .
pytest --cov=app --cov-fail-under=80
```
