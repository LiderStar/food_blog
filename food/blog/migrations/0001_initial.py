# Generated by Django 4.1.6 on 2023-02-03 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Не больше 100 символов",
                        max_length=100,
                        verbose_name="Название",
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="children",
                        to="blog.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Создать категорию",
                "verbose_name_plural": "Создать категории",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_index=True,
                        help_text="Не больше 256 символов",
                        max_length=256,
                        verbose_name="Название",
                    ),
                ),
                ("text", models.TextField(verbose_name="Описание")),
                (
                    "image",
                    models.ImageField(
                        default="blank-profile-picture.png",
                        upload_to="media/%Y/%m/%D/",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "create_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="posts",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="post",
                        to="blog.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Создать пост",
                "verbose_name_plural": "Создать посты",
                "ordering": ["create_at"],
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Не больше 100 символов",
                        max_length=100,
                        verbose_name="Тэг",
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "verbose_name": "Создать тєг",
                "verbose_name_plural": "Создать тєги",
            },
        ),
        migrations.CreateModel(
            name="Recepi",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=100, verbose_name="Название"
                    ),
                ),
                ("serv", models.CharField(max_length=50, verbose_name="Кол-во персон")),
                (
                    "prep_time",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Время подготовки"
                    ),
                ),
                (
                    "cook_time",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Время приготовления"
                    ),
                ),
                ("ingridients", models.TextField(verbose_name="Ингридиенты")),
                ("direction", models.TextField(verbose_name="Рецепт")),
                (
                    "post",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="recepi",
                        to="blog.post",
                    ),
                ),
            ],
            options={
                "verbose_name": "Создать рецепт",
                "verbose_name_plural": "Создать рецепты",
            },
        ),
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(related_name="post", to="blog.tag"),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Имя")),
                ("email", models.EmailField(max_length=254, verbose_name="Почта")),
                ("website", models.CharField(max_length=100, verbose_name="Сайт")),
                ("message", models.TextField(max_length=500, verbose_name="Текст")),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment",
                        to="blog.post",
                    ),
                ),
            ],
            options={
                "verbose_name": "Создать коментарий",
                "verbose_name_plural": "Создать коментарии",
            },
        ),
    ]
