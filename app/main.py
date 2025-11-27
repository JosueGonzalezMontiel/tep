import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers.personal import router as personal_router
from app.api.routers.recursos_m import router as recursos_m_router

from app.db.peewee_conn import db_session
from app.models.personal import Personal
from app.models.recursos_m import recursos_m
from app.db.peewee_conn import database
from app.api.routers.mantenimiento import router as mantenimiento_router
from app.api.routers.caracteristicas import router as caracteristicas_router
from app.models.mantenimiento import Mantenimiento
from app.models.caracteristicas import Caracteristicas

app = FastAPI(title="API RH", version="1.0.0")

origins = [
    "https://graymaya.shop",
    "http://graymaya.shop",
    "http://localhost",  
]

# permitir acceso desde frontend (ajusta los orígenes en variables de entorno en producción)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
