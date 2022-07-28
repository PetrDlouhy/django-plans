# Generated by Django 3.0.5 on 2020-04-15 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0004_create_user_plans'),
    ]

    operations = [
        migrations.AddField(
            model_name='planpricing',
            name='has_automatic_renewal',
            field=models.BooleanField(default=False, help_text='Use automatic renewal if possible?', verbose_name='has automatic renewal'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='order',
            field=models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='quota',
            name='order',
            field=models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order'),
        ),
        migrations.CreateModel(
            name='RecurringUserPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, default=None, help_text='Token, that will be used for payment renewal. Depends on used payment provider', max_length=255, null=True, verbose_name='recurring token')),
                ('payment_provider', models.CharField(blank=True, default=None, help_text='Provider, that will be used for payment renewal', max_length=255, null=True, verbose_name='payment provider')),
                ('amount', models.DecimalField(blank=True, db_index=True, decimal_places=2, max_digits=7, null=True, verbose_name='amount')),
                ('tax', models.DecimalField(blank=True, db_index=True, decimal_places=2, max_digits=4, null=True, verbose_name='tax')),
                ('currency', models.CharField(max_length=3, verbose_name='currency')),
                ('has_automatic_renewal', models.BooleanField(default=False, help_text='Automatic renewal is enabled for associated plan. If False, the plan renewal can be still initiated by user.', verbose_name='has automatic plan renewal')),
                ('card_expire_year', models.IntegerField(blank=True, null=True)),
                ('card_expire_month', models.IntegerField(blank=True, null=True)),
                ('pricing', models.ForeignKey(blank=True, default=None, help_text='Recurring pricing', null=True, on_delete=django.db.models.deletion.CASCADE, to='plans.Pricing')),
                ('user_plan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='recurring', to='plans.UserPlan')),
            ],
        ),
    ]
