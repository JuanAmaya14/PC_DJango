from django.db import models
from django.db.models.fields import CharField, IntegerField

class procesadores (models.Model):
    marca = CharField(max_length=50)
    modelo = CharField(max_length=50)
    precio = IntegerField()

class rams (models.Model):
    marca = CharField(max_length=50)
    cant_unidades_data = IntegerField()
    tipo_unidad = CharField(max_length=10, default="GB")
    precio = IntegerField()


class almacenamiento (models.Model):
    marca = CharField(max_length=50)
    cant_almacenamiento = IntegerField()
    tipo_unidad = CharField(max_length=10)
    forma_almacen = CharField(max_length=5)
    precio = IntegerField()


class Targetas_video (models.Model):
    marca = CharField(max_length=50)
    modelo = CharField(max_length=50)
    precio = IntegerField()


class pc_armadas (models.Model):
    marca = CharField(max_length=50)
    procesador = CharField(max_length=50)
    ram = CharField(max_length=30)
    t_video = CharField(default = "No tiene", max_length=50)
    rom = CharField(max_length=30)
    precio = IntegerField()



 