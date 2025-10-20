# app/models/mantenimiento.py
from peewee import Model, AutoField, CharField, DateField, ForeignKeyField
from app.db.peewee_conn import database
from app.models.recursos_m import recursos_m
from app.models.personal import Personal

class Mantenimiento(Model):
    id = AutoField()  # PK autoincremental
    nu_inventario = ForeignKeyField(
        recursos_m, column_name='nu_inventario',
        field='nu_inventario', on_delete='CASCADE', on_update='CASCADE'
    )
    fecha = DateField()
    trabajo = CharField(max_length=150)
    fallas = CharField(max_length=150)
    estatus = CharField(max_length=100)
    observaciones = CharField(max_length=200, null=True)
    responsable = ForeignKeyField(
        Personal, column_name='responsable',
        field='expediente', on_delete='CASCADE', on_update='CASCADE'
    )

    class Meta:
        database = database
        table_name = "mantenimiento"

# app/models/caracteristicas.py

