# Generated by Django 5.1.1 on 2024-10-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dogs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="breed",
            name="name",
            field=models.CharField(
                max_length=100, unique=True, verbose_name="Название породы"
            ),
        ),
    ]
