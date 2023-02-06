from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def pslist(request):
    return render(request, 'blog/food-list.html')


class PostList(ListView):
    model = Post
    # paginate_by = 50
    template_name = 'blog/food-list.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        return Post.objects.select_related('category').filter(category__slug=self.kwargs.get("slug"))


class HomeListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'list_posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-create_at')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/food-single.html'
    context_object_name = 'detail_post'
    slug_url_kwarg = 'post_slug'

