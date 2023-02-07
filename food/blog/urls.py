from django.urls import path

from blog import views
from blog.views import PostList, HomeListView, PostDetailView, CategoryList

urlpatterns = [
    path('', HomeListView.as_view(), name="index"),
    path('<slug:slug>/', PostList.as_view(), name="food_list"),
    # path('<slug:category_slug>/', CategoryList.as_view(), name="category_list"),
    path('<slug:slug>/<slug:post_slug>', PostDetailView.as_view(), name="food_single"),
    # path('all/', views.pslist, name="post_list"),
]