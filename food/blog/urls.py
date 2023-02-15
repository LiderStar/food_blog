from django.urls import path

from blog import views
from blog.views import PostList, HomeListView, PostDetailView, CategoryListView, TagsListView, SearchView, CreateComment

urlpatterns = [
    path('comment/<int:pk>', CreateComment.as_view(), name="create_comment"),
    path('search/', SearchView.as_view(), name="search"),
    path('<slug:slug>/', PostList.as_view(), name="food_list"),
    path('<slug:slug>/', CategoryListView.as_view(), name="category_list"),
    path('tags/<slug:slug>/', TagsListView.as_view(), name="tags"),
    path('<slug:slug>/<slug:post_slug>/', PostDetailView.as_view(), name="food_single"),
    path('', HomeListView.as_view(), name="index"),
]
