# Generated by Django 5.1.1 on 2025-02-24 07:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0003_alter_event_time'),
        ('Registrations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Events.event'),
        ),
    ]
