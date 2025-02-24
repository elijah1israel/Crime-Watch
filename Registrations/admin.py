from django.contrib import admin
from .models import Registration

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'contact_person')
    search_fields = ('company_name', 'contact_person')
    list_filter = ('company_name', 'event__title')

