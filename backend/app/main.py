from fastapi import FastAPI

from app.routes import work_orders, intake_records, cleaning_procedures, work_plans

app = FastAPI(
    title="Process Execution System",
    description="Aerospace precision cleaning operations management",
    version="1.0.0",
)

app.include_router(work_orders.router)
app.include_router(intake_records.router)
app.include_router(cleaning_procedures.router)
app.include_router(work_plans.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
