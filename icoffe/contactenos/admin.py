from django.contrib import admin
from .models import Contacto
# Register your models here.

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    pass