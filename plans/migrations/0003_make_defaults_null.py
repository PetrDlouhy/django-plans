# Generated by Django 2.0.6 on 2018-08-24 14:21

from django.db import migrations

def set_default_null(apps, schema_editor):
    Plan = apps.get_model("plans", "Plan")
    Plan.objects.filter(default=False).update(default=None)

class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_default_nullboolean'),
    ]

    operations = [
        migrations.RunPython(set_default_null),
    ]