from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date', 'time')
    search_fields = ('title', 'location')
    list_filter = ('date', 'time')
    ordering = ('-date', '-time')
