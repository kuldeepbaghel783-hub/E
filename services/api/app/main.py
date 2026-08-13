from fastapi import FastAPI

app = FastAPI(
    title="eSports Tournament Platform API",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "esports-api",
    }