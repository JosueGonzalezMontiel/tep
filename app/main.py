import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers.personal import router as personal_router
from app.api.routers.recursos_m import router as recursos_m_router
from app.core.config import CORS_ORIGINS
from app.db.peewee_conn import db_session
from app.models.personal import Personal
from app.models.recursos_m import recursos_m
from app.db.peewee_conn import database
import logging
from app.api.routers.mantenimiento import router as mantenimiento_router
from app.api.routers.caracteristicas import router as caracteristicas_router
from app.models.mantenimiento import Mantenimiento
from app.models.caracteristicas import Caracteristicas

app = FastAPI(title="API RH", version="1.0.0")

CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost").split(",")

# permitir acceso desde frontend (ajusta los orígenes en variables de entorno en producción)
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
logging.getLogger("uvicorn").info(f"CORS_ORIGINS={CORS_ORIGINS}")

# Registrar routers
app.include_router(personal_router)
app.include_router(recursos_m_router)
app.include_router(mantenimiento_router)
app.include_router(caracteristicas_router)
# Eventos de app: abrir/cerrar conexión por ciclo de vida
@app.on_event("startup")
def on_startup():
    db_session()
    # Crear tablas si no existen (en producción normalmente migraciones)
    database.create_tables([Personal,recursos_m, Mantenimiento, Caracteristicas], safe=True)

@app.on_event("shutdown")
def on_shutdown():
    db_session()
