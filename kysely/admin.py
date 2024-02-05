# Register your models here.
from django.contrib import admin

from .models import Kysymys, Vaihtoehto

admin.site.register(Kysymys)

@admin.site.register(Vaihtoehto)
class VaihtoehtoAdmin(admin.ModelAdmin):
    list_display = ["Kysymys", "teksti"]
