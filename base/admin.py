from django.contrib import admin
from .models import God, Product, Hero, Creature, User, Type, Image, Comment
# Register your models here.


admin.site.register(God)
admin.site.register(Product)
admin.site.register(Hero)
admin.site.register(Creature)
admin.site.register(User)
admin.site.register(Type)
admin.site.register(Image)
admin.site.register(Comment)


class GodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    search_fields = ('name',)
