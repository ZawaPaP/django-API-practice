# Generated by Django 4.2.2 on 2023-06-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projects",
            name="created_at",
            field=models.DateField(),
        ),
    ]