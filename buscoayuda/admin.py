from django.contrib import admin

# Register your models here.
from buscoayuda.models import TiposDeServicio


class TiposDeServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(TiposDeServicio, TiposDeServicioAdmin)