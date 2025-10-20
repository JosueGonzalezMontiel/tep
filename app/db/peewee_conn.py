from peewee import MySQLDatabase
from playhouse.shortcuts import model_to_dict
from app.core.config import settings

database = MySQLDatabase(
    settings.DB_NAME,
    user=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
)

# Hooks para FastAPI: abrir/cerrar conexión por petición
class db_session:    
    def connect_db():
        if database.is_closed():
            database.connect(reuse_if_open=True)

    def close_db(exc=None):
        if not database.is_closed():
            database.close()

# Helper para serializar modelos Peewee -> dict (evita repetir)
def to_dict(instance, **kwargs):
    return model_to_dict(instance, recurse=False, **kwargs)
