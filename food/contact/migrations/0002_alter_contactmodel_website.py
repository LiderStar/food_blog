# Generated by Django 4.1.6 on 2023-02-13 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactmodel",
            name="website",
            field=models.URLField(blank=True, null=True, verbose_name="Сайт"),
        ),
    ]
