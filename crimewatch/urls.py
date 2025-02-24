from django.contrib import admin
from django.urls import path
from .views import index, get_template, register_event

urlpatterns = [
    path('', index),
    path('<str:template_name>', get_template),
    path('register/<int:event_id>', register_event, name='event_register'),
    path('admin/', admin.site.urls),
]

