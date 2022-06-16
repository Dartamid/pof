from django.contrib import admin
from .models import Guide, Paragraph


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    empty_value_display = '--пусто--'

@admin.register(Paragraph)
class ParagraphAdmin(admin.ModelAdmin):
    empty_value_display = '--пусто--'