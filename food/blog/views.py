from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post, Category, Tag


class HomeListView(ListView):
    ''' Закгружаем стартовую страницу сортируя посты по дате создания '''
    model = Post
    paginate_by = 9
    template_name = 'blog/index.html'
    context_object_name = 'list_posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-create_at')

class PostList(ListView):
    ''' Закгружаем страницу с выборкой постов по категории '''
    model = Post
    paginate_by = 9
    template_name = 'blog/food-list.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        return Post.objects.select_related('category').filter(category__slug=self.kwargs.get("slug"))


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/food-single.html'
    context_object_name = 'detail_post'
    slug_url_kwarg = 'post_slug'


class CategoryListView(ListView):
    ''' Закгружаем стартовую страницу сортируя посты по дате создания '''
    model = Category
    paginate_by = 9
    template_name = 'blog/index.html'
    context_object_name = 'category_list'


# class TagsListView(ListView):
#     model = Post
#     paginate_by = 9
#     template_name = 'blog/index.html'
#     context_object_name = 'all_posts'
#
#     def get_queryset(self):
#         return Post.objects.filter(tags__slug=self.kwargs["slug"])
#
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Записи по  тэгу' + str(Tag.objects.get(slug=self.kwargs['slug']))


class TagsListView(ListView):
    ''' Закгружаем страницу с выборкой постов по категории '''
    model = Post
    paginate_by = 9
    template_name = 'blog/food-list.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        # return Post.objects.select_related('tag').filter(tags__slug=self.kwargs.get("slug"))
        return Post.objects.filter(tags__slug=self.kwargs.get("slug"))

