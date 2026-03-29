from fastapi import FastAPI
from src.routes.health import router as health_router
from src.routes.notes import router as notes_router
app = FastAPI()
app.include_router(health_router)
app.include_router(notes_router, prefix='/api', tags=['notes'])