from django.contrib import admin
from .models import procesadores, rams, almacenamiento, Targetas_video, pc_armadas

class procesador_admin (admin.ModelAdmin):
    list_display = ["marca", "modelo", "precio"]

class ram_admin (admin.ModelAdmin):
    list_display = ["marca", "cant_unidades_data", "tipo_unidad", "precio"]

class almacenamiento_admin (admin.ModelAdmin):
    list_display = ["marca", "cant_almacenamiento", "tipo_unidad", "forma_almacen", "precio"]

class video_admin (admin.ModelAdmin):
    list_display = ["marca", "modelo", "precio"]

class pcs_admin (admin.ModelAdmin):
    list_display = ["marca", "procesador", "ram", "t_video", "rom", "precio"]


# Register your models here.
admin.site.register(procesadores, procesador_admin)
admin.site.register(rams, ram_admin)
admin.site.register(almacenamiento, almacenamiento_admin)
admin.site.register(Targetas_video, video_admin)
admin.site.register(pc_armadas, pcs_admin)