from fastapi import FastAPI

app = FastAPI(title="Mini API")


@app.get("/sante")
def sante():
    return {"statut": "ok"}
