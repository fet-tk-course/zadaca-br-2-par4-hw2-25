from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_db_and_tables

import models_a
import models_b


from routes_a import router as router_a


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="Zadaća 2 - REST API",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(router_a)    # Ukljucivanje ruta za resurs A


@app.get("/")
def read_root():
    return {"message": "Zadaća 2 - REST API"}