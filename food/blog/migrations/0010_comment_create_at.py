# Generated by Django 4.1.6 on 2023-02-15 10:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_comment_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]