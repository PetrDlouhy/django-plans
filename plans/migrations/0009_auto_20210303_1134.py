# Generated by Django 3.0.13 on 2021-03-03 10:34

import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0008_recurringuserplan_token_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planquota',
            name='value',
            field=models.BigIntegerField(blank=True, default=1, null=True),
        ),
    ]
