from django.contrib import admin
from .models import God
# Register your models here.

admin.site.register(God)
class GodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    search_fields = ('name',)

