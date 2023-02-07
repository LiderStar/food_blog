from django import template

from blog.models import Category, Post

register = template.Library()

# @register.simple_tag()
# def get_categories():
#     '''Вывод всех категорий'''
#     return Category.objects.all()


@register.inclusion_tag("blog/include/tags/nav_menu.html")
def get_categories():
    category = Category.objects.filter(parent__isnull=True).order_by()
    return {"list_category":category}

