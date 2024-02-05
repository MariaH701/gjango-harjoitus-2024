from django.contrib import admin

# Register your models here.
from django.contrib import admin, Vaihtoehto

from .models import Kysymys, Vaihtoehto

admin.site.register(Kysymys)

admin.site.register(Vaihtoehto)
class VaihtoehtoAdmin(admin.ModelAdmin):
    list_display = ["Kysymys", "teksti"]
