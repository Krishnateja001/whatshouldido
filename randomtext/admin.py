from django.contrib import admin

from .models import ShortText


@admin.register(ShortText)
class ShortTextAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at')
    search_fields = ('text',)
