# Generated by Django 4.1.7 on 2023-03-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_alter_category_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brand",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
