# Generated by Django 4.1.6 on 2023-02-05 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_text_alter_recepi_direction_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(default=1, max_length=256, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(
                default="blank-profile-picture.png",
                upload_to="media/%Y/%m/%d/",
                verbose_name="Изображение",
            ),
        ),
    ]
