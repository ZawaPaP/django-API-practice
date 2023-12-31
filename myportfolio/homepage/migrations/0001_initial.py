# Generated by Django 4.2.2 on 2023-06-16 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Projects",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="projects/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
