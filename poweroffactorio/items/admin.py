from django.contrib import admin
from .models import ItemType, RequiredTechnology, \
    Effect, Ingredient, Item, Recipe, Linked


@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    empty_value_display = '--пусто--'


@admin.register(RequiredTechnology)
class RequiredTechnologyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    empty_value_display = '--пусто--'


@admin.register(Effect)
class EffectAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'value', 'time')
    empty_value_display = '--пусто--'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name', 'description',
    )
    empty_value_display = '--пусто--'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    empty_value_display = '--пусто--'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    empty_value_display = '--пусто--'


@admin.register(Linked)
class LinkedAdmin(admin.ModelAdmin):
    empty_value_display = '--пусто--'