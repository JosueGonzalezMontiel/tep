from peewee import Model, CharField, ForeignKeyField
from app.db.peewee_conn import database
from app.models.recursos_m import recursos_m

class Caracteristicas(Model):
    nu_inventario = ForeignKeyField(
        recursos_m, primary_key=True, column_name='nu_inventario',
        field='nu_inventario', on_delete='CASCADE', on_update='CASCADE'
    )
    nombre = CharField(max_length=150, null=True)
    ip = CharField(max_length=50, null=True)
    procesador = CharField(max_length=100, null=True)
    memoria = CharField(max_length=50, null=True)
    disco_duro = CharField(max_length=50, null=True)
    paqueterias = CharField(max_length=200, null=True)
    inv_anterio = CharField(max_length=50, null=True)

    class Meta:
        database = database
        table_name = "caracteristicas"