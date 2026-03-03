from fastapi import FastAPI

from app.routes import (
    work_orders,
    intake_records,
    cleaning_procedures,
    work_plans,
    section_groups,
    steps,
    substeps,
    step_field_definitions,
    step_field_entries,
    baths,
    records,
    equipment_logs,
    lab_maintenance_logs,
)

app = FastAPI(
    title="Process Execution System",
    description="Aerospace precision cleaning operations management",
    version="1.0.0",
)

app.include_router(work_orders.router)
app.include_router(intake_records.router)
app.include_router(cleaning_procedures.router)
app.include_router(work_plans.router)
app.include_router(section_groups.router)
app.include_router(steps.router)
app.include_router(substeps.router)
app.include_router(step_field_definitions.router)
app.include_router(step_field_entries.router)
app.include_router(baths.router)
app.include_router(records.router)
app.include_router(equipment_logs.router)
app.include_router(lab_maintenance_logs.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
