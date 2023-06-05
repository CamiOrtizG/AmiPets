from django.contrib import admin
from .models import Persona, Region, Comuna, Sucursal, Funcionario, ficha_pet, estado, reserva, Tarifa, estadia, Vacuna, Hist_pago, Hist_reserva

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display =["nombres"]
    search_fields =["nombres"]

class FuncionarioAdmin(admin.ModelAdmin):
    list_display =["persona","cargo"]
    list_filter=["persona"]

class ficha_petAdmin(admin.ModelAdmin):
    list_display =["nombre_pet","dueño"]
    search_fields =["nombres"]

class estadoAdmin(admin.ModelAdmin):
    list_display =["descrip_est"]

class estadiaAdmin(admin.ModelAdmin):
    list_display =["cliente","descrip_est"]    


admin.site.register(Persona, PersonaAdmin)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Sucursal)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(ficha_pet, ficha_petAdmin)
admin.site.register(estado)
admin.site.register(reserva)
admin.site.register(Tarifa)
admin.site.register(estadia, estadiaAdmin)
admin.site.register(Vacuna)
admin.site.register(Hist_pago)
admin.site.register(Hist_reserva)



