# Register your models here.
from django.contrib import admin

from .models import Kysymys, Vaihtoehto

class ChoiceInline(admin.TabularInline):
    model = Vaihtoehto
    extra = 3
    
@admin.register(Kysymys)
class KysymysAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Päivämäärätiedot", {"fields": ["julkaisupvm"]}),
        ("Sisältö", {"fields": ["teksti"]}),
    ]

@admin.register(Vaihtoehto)
class VaihtoehtoAdmin(admin.ModelAdmin):
    list_display = ["kysymys", "teksti"]
