from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField



class Category(MPTTModel):
    class Meta:
        verbose_name = 'Создать категорию'
        verbose_name_plural = "Создать категории"

    class MPTTMeta:
        order_insertion_by = ['name']

    name = models.CharField(max_length=100, help_text="Не больше 100 символов", verbose_name="Название")
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    parent = TreeForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    class Meta:
        verbose_name = 'Создать тєг'
        verbose_name_plural = "Создать тєги"

    name = models.CharField(max_length=100, help_text="Не больше 100 символов", verbose_name="Тэг")
    slug = models.SlugField(max_length=50, unique=True, db_index=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = "Создать посты"
        ordering = ['create_at']

    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=256, db_index=True, help_text="Не больше 256 символов", verbose_name="Название")
    text_present = RichTextField(max_length=300, verbose_name="Краткое описание", blank=True)
    text = RichTextField(verbose_name="Описание")
    image = models.ImageField(upload_to='media/%Y/%m/%d/', default='blank-profile-picture.png',
                              verbose_name="Изображение")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    category = models.ForeignKey(Category, related_name="post", on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name="post")
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('food_single', kwargs={'slug': self.category.slug, 'post_slug': self.slug })


class Recepi(models.Model):
    class Meta:
        verbose_name = 'Создать рецепт'
        verbose_name_plural = "Создать рецепты"


    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    serv = models.CharField(max_length=50, verbose_name='Кол-во персон')
    prep_time = models.PositiveIntegerField(default=0, verbose_name='Время подготовки')
    cook_time = models.PositiveIntegerField(default=0, verbose_name='Время приготовления')
    ingridients = RichTextField(verbose_name='Ингридиенты')
    direction = RichTextField(verbose_name='Рецепт')
    post = models.ForeignKey(Post, related_name='recepi', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    class Meta:
        verbose_name = 'Создать коментарий'
        verbose_name_plural = "Создать коментарии"


    name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    website = models.CharField(max_length=100, verbose_name='Сайт')
    message = models.TextField(max_length=500, verbose_name='Текст')
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

