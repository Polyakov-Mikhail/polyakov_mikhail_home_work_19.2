# Generated by Django 5.1 on 2024-09-26 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="count_views",
            field=models.PositiveIntegerField(default=0, verbose_name="Просмотры"),
        ),
    ]
