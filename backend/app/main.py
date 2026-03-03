from fastapi import FastAPI

app = FastAPI(
    title="Process Execution System",
    description="Aerospace precision cleaning operations management",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}
