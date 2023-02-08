from django import template

from blog.models import Category, Post, Tag

register = template.Library()


@register.inclusion_tag("blog/include/tags/nav_menu.html")
def get_categories():
    category = Category.objects.order_by()
    return {"list_category": category}


@register.inclusion_tag("blog/include/tags/had_menu.html")
def get_categories_nav():
    category = Category.objects.order_by()
    return {"nav_category": category}

@register.inclusion_tag("blog/include/tags/last_post.html")
def get_last_post():
    category = Post.objects.order_by("-id")[0:4]
    return {"last_post": category}


@register.inclusion_tag("blog/include/tags/tags_list.html")
def get_tags_list():
    tg = Tag.objects.order_by()
    return {"tags_list": tg}

