from peewee import Model, IntegerField, CharField, DateField, TextField, ForeignKeyField
from app.db.peewee_conn import database
from app.models.personal import Personal

class recursos_m(Model):
    nu_inventario = CharField(primary_key=True)   # PK
    nu_NSAR = CharField(max_length=100) # INVNETARIO SISTEMAS 
    descripcion = CharField(max_length=200, null=True)
    marca = CharField(max_length=150)
    modelo = CharField(max_length=150)
    serie = CharField(max_length=150)
    observaciones = CharField(max_length=200, null=True)
    material = CharField(max_length=150, null=True)
    color = CharField(max_length=100, null=True)
    estado_ficico = CharField(max_length=100, null=True)
    ubicacion = CharField(max_length=150, null=True)
    expediente_resguardo = ForeignKeyField(
        Personal,
        column_name='expediente_resguardo',
        field='expediente',          # FK → PK del modelo Personal
        on_delete='CASCADE',         # elimina recursos si se borra el personal
        on_update='CASCADE',
        null=True
    )
    fecha_asig = DateField(null=True)
    ruta = TextField(null=True)

    class Meta:
        database = database
        table_name = "resursos_m"