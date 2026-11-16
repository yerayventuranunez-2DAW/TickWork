from django.contrib import admin
from .models import Zona, Usuario, Conserje, Ubicacion, Aviso

# Register your models here.

admin.site.register(Zona)
admin.site.register(Usuario)
admin.site.register(Conserje)
admin.site.register(Ubicacion)
admin.site.register(Aviso)