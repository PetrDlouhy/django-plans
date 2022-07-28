# Generated by Django 4.0.6 on 2022-07-28 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0011_auto_20220208_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='planpricing',
            name='visible',
            field=models.BooleanField(default=True, help_text='Is visible in current offer', verbose_name='is visible by default'),
        ),
    ]