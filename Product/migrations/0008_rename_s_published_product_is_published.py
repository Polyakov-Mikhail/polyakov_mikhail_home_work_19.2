# Generated by Django 4.2.2 on 2024-10-20 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Product", "0007_product_s_published"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="s_published",
            new_name="is_published",
        ),
    ]
