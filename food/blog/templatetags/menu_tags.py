from django import template
from blog.models import Category, Post, Tag, Comment

register = template.Library()


@register.inclusion_tag("blog/include/tags/nav_side.html")
def get_categories(tag_template):
    '''Мы передаем параметр для того что-бы использовать один тэг в разных шаблонах
    nav_side - основной шаблон а другие в которых нужен этот контекст его наследуют
    вызов {% get_categories 'blog/include/tags/nav_menu.html' %} '''
    category = Category.objects.order_by()
    return {"tag_template": tag_template, "list_category": category}

@register.inclusion_tag("blog/include/tags/last_post.html")
def get_last_post(cnt=4):
    posts = Post.objects.order_by("-views")[:cnt]
    return {"posts": posts}


@register.inclusion_tag("blog/include/tags/tags_list.html")
def get_tags_list():
    tg = Tag.objects.order_by()
    return {"tags_list": tg}


# @register.simple_tag()
# def new_tag(request):
#     path = request.path.split("/")
#     if len(path) <= 3:
#         return {"tag_1": str(path[1])}
#     else:
#         return {"tag_1": str(path[1]), "tag_n": str(path[2])}

