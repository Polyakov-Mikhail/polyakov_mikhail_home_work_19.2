# Generated by Django 5.1 on 2024-09-24 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Product", "0002_product_manufactured_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="manufactured_at",
        ),
    ]