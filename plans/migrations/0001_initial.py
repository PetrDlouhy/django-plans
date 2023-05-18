# Generated by Django 2.0.6 on 2018-06-12 12:30

from decimal import Decimal

import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BillingInfo",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tax_number",
                    models.CharField(
                        blank=True, db_index=True, max_length=200, verbose_name="VAT ID"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=200, verbose_name="name"
                    ),
                ),
                ("street", models.CharField(max_length=200, verbose_name="street")),
                ("zipcode", models.CharField(max_length=200, verbose_name="zip code")),
                ("city", models.CharField(max_length=200, verbose_name="city")),
                (
                    "country",
                    django_countries.fields.CountryField(
                        max_length=2, verbose_name="country"
                    ),
                ),
                (
                    "shipping_name",
                    models.CharField(
                        blank=True,
                        help_text="optional",
                        max_length=200,
                        verbose_name="name (shipping)",
                    ),
                ),
                (
                    "shipping_street",
                    models.CharField(
                        blank=True,
                        help_text="optional",
                        max_length=200,
                        verbose_name="street (shipping)",
                    ),
                ),
                (
                    "shipping_zipcode",
                    models.CharField(
                        blank=True,
                        help_text="optional",
                        max_length=200,
                        verbose_name="zip code (shipping)",
                    ),
                ),
                (
                    "shipping_city",
                    models.CharField(
                        blank=True,
                        help_text="optional",
                        max_length=200,
                        verbose_name="city (shipping)",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "Billing info",
                "verbose_name_plural": "Billing infos",
            },
        ),
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.IntegerField(db_index=True)),
                ("full_number", models.CharField(max_length=200)),
                (
                    "type",
                    models.IntegerField(
                        choices=[
                            (1, "Invoice"),
                            (2, "Invoice Duplicate"),
                            (3, "Order confirmation"),
                        ],
                        db_index=True,
                        default=1,
                    ),
                ),
                ("issued", models.DateField(db_index=True)),
                (
                    "issued_duplicate",
                    models.DateField(blank=True, db_index=True, null=True),
                ),
                (
                    "selling_date",
                    models.DateField(blank=True, db_index=True, null=True),
                ),
                ("payment_date", models.DateField(db_index=True)),
                ("unit_price_net", models.DecimalField(decimal_places=2, max_digits=7)),
                ("quantity", models.IntegerField(default=1)),
                ("total_net", models.DecimalField(decimal_places=2, max_digits=7)),
                ("total", models.DecimalField(decimal_places=2, max_digits=7)),
                ("tax_total", models.DecimalField(decimal_places=2, max_digits=7)),
                (
                    "tax",
                    models.DecimalField(
                        blank=True,
                        db_index=True,
                        decimal_places=2,
                        max_digits=4,
                        null=True,
                    ),
                ),
                (
                    "rebate",
                    models.DecimalField(
                        decimal_places=2, default=Decimal("0"), max_digits=4
                    ),
                ),
                ("currency", models.CharField(default="EUR", max_length=3)),
                ("item_description", models.CharField(max_length=200)),
                ("buyer_name", models.CharField(max_length=200, verbose_name="Name")),
                (
                    "buyer_street",
                    models.CharField(max_length=200, verbose_name="Street"),
                ),
                (
                    "buyer_zipcode",
                    models.CharField(max_length=200, verbose_name="Zip code"),
                ),
                ("buyer_city", models.CharField(max_length=200, verbose_name="City")),
                (
                    "buyer_country",
                    django_countries.fields.CountryField(
                        default="PL", max_length=2, verbose_name="Country"
                    ),
                ),
                (
                    "buyer_tax_number",
                    models.CharField(
                        blank=True, max_length=200, verbose_name="TAX/VAT number"
                    ),
                ),
                (
                    "shipping_name",
                    models.CharField(max_length=200, verbose_name="Name"),
                ),
                (
                    "shipping_street",
                    models.CharField(max_length=200, verbose_name="Street"),
                ),
                (
                    "shipping_zipcode",
                    models.CharField(max_length=200, verbose_name="Zip code"),
                ),
                (
                    "shipping_city",
                    models.CharField(max_length=200, verbose_name="City"),
                ),
                (
                    "shipping_country",
                    django_countries.fields.CountryField(
                        default="PL", max_length=2, verbose_name="Country"
                    ),
                ),
                ("require_shipment", models.BooleanField(db_index=True, default=False)),
                ("issuer_name", models.CharField(max_length=200, verbose_name="Name")),
                (
                    "issuer_street",
                    models.CharField(max_length=200, verbose_name="Street"),
                ),
                (
                    "issuer_zipcode",
                    models.CharField(max_length=200, verbose_name="Zip code"),
                ),
                ("issuer_city", models.CharField(max_length=200, verbose_name="City")),
                (
                    "issuer_country",
                    django_countries.fields.CountryField(
                        default="PL", max_length=2, verbose_name="Country"
                    ),
                ),
                (
                    "issuer_tax_number",
                    models.CharField(
                        blank=True, max_length=200, verbose_name="TAX/VAT number"
                    ),
                ),
            ],
            options={
                "verbose_name": "Invoice",
                "verbose_name_plural": "Invoices",
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("flat_name", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "created",
                    models.DateTimeField(db_index=True, verbose_name="created"),
                ),
                (
                    "completed",
                    models.DateTimeField(
                        blank=True, db_index=True, null=True, verbose_name="completed"
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        db_index=True,
                        decimal_places=2,
                        max_digits=7,
                        verbose_name="amount",
                    ),
                ),
                (
                    "tax",
                    models.DecimalField(
                        blank=True,
                        db_index=True,
                        decimal_places=2,
                        max_digits=4,
                        null=True,
                        verbose_name="tax",
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        default="EUR", max_length=3, verbose_name="currency"
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (1, "new"),
                            (2, "completed"),
                            (3, "not valid"),
                            (4, "canceled"),
                            (5, "returned"),
                        ],
                        default=1,
                        verbose_name="status",
                    ),
                ),
            ],
            options={
                "verbose_name": "Order",
                "verbose_name_plural": "Orders",
                "ordering": ("-created",),
            },
        ),
        migrations.CreateModel(
            name="Plan",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order", models.PositiveIntegerField(db_index=True, editable=False)),
                ("name", models.CharField(max_length=100, verbose_name="name")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
                ("default", models.BooleanField(db_index=True, default=False)),
                (
                    "available",
                    models.BooleanField(
                        db_index=True,
                        default=False,
                        help_text="Is still available for purchase",
                        verbose_name="available",
                    ),
                ),
                (
                    "visible",
                    models.BooleanField(
                        db_index=True,
                        default=True,
                        help_text="Is visible in current offer",
                        verbose_name="visible",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(db_index=True, verbose_name="created"),
                ),
                (
                    "url",
                    models.URLField(
                        blank=True,
                        help_text="Optional link to page with more information (for clickable pricing table headers)",
                    ),
                ),
                (
                    "customized",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="customized",
                    ),
                ),
            ],
            options={
                "verbose_name": "Plan",
                "verbose_name_plural": "Plans",
                "ordering": ("order",),
            },
        ),
        migrations.CreateModel(
            name="PlanPricing",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(db_index=True, decimal_places=2, max_digits=7),
                ),
                (
                    "plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="plans.Plan"
                    ),
                ),
            ],
            options={
                "verbose_name": "Plan pricing",
                "verbose_name_plural": "Plans pricings",
                "ordering": ("pricing__period",),
            },
        ),
        migrations.CreateModel(
            name="PlanQuota",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.IntegerField(blank=True, default=1, null=True)),
                (
                    "plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="plans.Plan"
                    ),
                ),
            ],
            options={
                "verbose_name": "Plan quota",
                "verbose_name_plural": "Plans quotas",
            },
        ),
        migrations.CreateModel(
            name="Pricing",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="name")),
                (
                    "period",
                    models.PositiveIntegerField(
                        blank=True,
                        db_index=True,
                        default=30,
                        null=True,
                        verbose_name="period",
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        blank=True,
                        help_text="Optional link to page with more information (for clickable pricing table headers)",
                    ),
                ),
            ],
            options={
                "verbose_name": "Pricing",
                "verbose_name_plural": "Pricings",
                "ordering": ("period",),
            },
        ),
        migrations.CreateModel(
            name="Quota",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order", models.PositiveIntegerField(db_index=True, editable=False)),
                (
                    "codename",
                    models.CharField(
                        db_index=True,
                        max_length=50,
                        unique=True,
                        verbose_name="codename",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="name")),
                (
                    "unit",
                    models.CharField(blank=True, max_length=100, verbose_name="unit"),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
                (
                    "is_boolean",
                    models.BooleanField(default=False, verbose_name="is boolean"),
                ),
                (
                    "url",
                    models.CharField(
                        blank=True,
                        help_text="Optional link to page with more information (for clickable pricing table headers)",
                        max_length=200,
                    ),
                ),
            ],
            options={
                "verbose_name": "Quota",
                "verbose_name_plural": "Quotas",
                "ordering": ("order",),
            },
        ),
        migrations.CreateModel(
            name="UserPlan",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "expire",
                    models.DateField(
                        blank=True,
                        db_index=True,
                        default=None,
                        null=True,
                        verbose_name="expire",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        db_index=True, default=True, verbose_name="active"
                    ),
                ),
                (
                    "plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plans.Plan",
                        verbose_name="plan",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "User plan",
                "verbose_name_plural": "Users plans",
            },
        ),
        migrations.AddField(
            model_name="planquota",
            name="quota",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="plans.Quota"
            ),
        ),
        migrations.AddField(
            model_name="planpricing",
            name="pricing",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="plans.Pricing"
            ),
        ),
        migrations.AddField(
            model_name="plan",
            name="quotas",
            field=models.ManyToManyField(through="plans.PlanQuota", to="plans.Quota"),
        ),
        migrations.AddField(
            model_name="order",
            name="plan",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="plan_order",
                to="plans.Plan",
                verbose_name="plan",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="pricing",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="plans.Pricing",
                verbose_name="pricing",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="plans.Order",
                verbose_name="order",
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
    ]
