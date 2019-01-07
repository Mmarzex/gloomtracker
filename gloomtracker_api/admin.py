from django.contrib import admin
from .models import CharacterClass, Character, Item, Perk

# Register your models here.

admin.site.register(CharacterClass)
admin.site.register(Character)
admin.site.register(Item)
admin.site.register(Perk)
