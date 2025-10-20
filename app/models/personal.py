from peewee import Model, IntegerField, CharField, DateField, TextField
from app.db.peewee_conn import database

class Personal(Model):
    expediente = IntegerField(primary_key=True)   # PK
    paterno = CharField(max_length=100)
    materno = CharField(max_length=100, null=True)
    nombre = CharField(max_length=150)
    f_nacimiento = DateField(null=True)
    estado_civil = CharField(max_length=20, null=True)
    adscripcion = CharField(max_length=150, null=True)
    cargo = CharField(max_length=150, null=True)
    ruta = TextField(null=True)

    class Meta:
        database = database
        table_name = "personal"

