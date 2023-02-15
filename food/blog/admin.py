from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin

from blog.models import Category, Tag, Post, Recepi, Comment
from django import forms


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class RecipeInline(admin.StackedInline):  # добавляет в админке к модели пост поля модели рецепты
    model = Recepi
    extra = 1


class PostAdmin(admin.ModelAdmin):
    save_as = True  # Должна изменить кнопку но нет  (((((
    save_on_top = True

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'


# Register your models here.
@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'slug']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ('name',)


@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ('name',)


@admin.register(Post)
class AdminPost(PostAdmin, PostAdminForm):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'author', 'create_at', 'category', 'get_photo']
    list_display_links = ['author', 'title']  # поля в виде ссылок
    search_fields = ['author', 'title']  # поля поиска
    list_filter = ('category', 'title', 'tags')
    readonly_fields = ('create_at', 'get_photo', 'views')  # поля только для чтения
    fields = ['title', 'slug', 'category', 'author', 'tags', 'text_present', 'text', 'image', 'get_photo', 'views',
              'create_at']  # очередность полей уже в открытом посте
    save_as = True
    inlines = [RecipeInline]


@admin.register(Recepi)
class AdminRecepi(admin.ModelAdmin, PostAdminForm):
    class Meta:
        model = Recepi
        fields = '__all__'

    list_display = ['name', 'serv', 'prep_time', 'cook_time', 'post']
    list_display_links = ['name', 'post']
    search_fields = ['name']
    list_filter = ('name',)


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ['name', 'email', 'website', 'create_at', 'id']
    list_display_links = ['name', 'email', 'website']
    search_fields = ['name', 'email']
    list_filter = ('name', 'email',)
    save_as = True  # Должна изменить кнопку но нет  (((((
