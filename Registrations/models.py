from django.db import models
from Events.models import Event

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=255)
    company_address = models.TextField()
    fax_number = models.CharField(max_length=20)
    telephone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    contact_person = models.CharField(max_length=255)
    contact_person_telephone_number = models.CharField(max_length=20)
    managing_director = models.CharField(max_length=255)
    managing_director_telephone_number = models.CharField(max_length=20)
    managing_director_email = models.EmailField()
    products = models.TextField()
    services = models.TextField()

