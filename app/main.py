from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/healthchecker")
def root():
    return {"msg": "API app and running"}
