from fastapi import FastAPI

app = FastAPI(title="Starter")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}
