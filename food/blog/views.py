from django.http import HttpRequest, request
from django.shortcuts import render
from django.urls import resolve
from django.views.generic import ListView, DetailView
from django.template import RequestContext

from .models import Post, Category, Tag
from django.db.models import F


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

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/food-single.html'
    context_object_name = 'detail_post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


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


class SearchView(ListView):
    model = Post
    paginate_by = 9
    template_name = 'blog/search-list.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        search_term = self.request.GET.get('s')
        if search_term:
            return Post.objects.filter(title__icontains=search_term)
        return Post.objects.all()

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
