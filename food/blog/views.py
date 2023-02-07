from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post, Category


class HomeListView(ListView):
    ''' Закгружаем стартовую страницу сортируя посты по дате создания '''
    model = Post
    paginate_by = 25
    template_name = 'blog/index.html'
    context_object_name = 'list_posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-create_at')

class PostList(ListView):
    ''' Закгружаем страницу с выборкой постов по категории '''
    model = Post
    paginate_by = 25
    template_name = 'blog/food-list.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        return Post.objects.select_related('category').filter(category__slug=self.kwargs.get("slug"))


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/food-single.html'
    context_object_name = 'detail_post'
    slug_url_kwarg = 'post_slug'


class CategoryList(ListView):
    model = Category
    # paginate_by = 50
    template_name = 'blog/food-list.html'
    context_object_name = 'all_category'

    def get_queryset(self):
        return Category.objects.all()
