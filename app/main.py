from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/healthchecker")
def root() -> dict[str, str]:
    return {"msg": "API app and running"}
