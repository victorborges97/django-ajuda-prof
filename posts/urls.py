from django.contrib import admin
from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    # path('', views.HomePageView.as_view(), name="home"),
    path('', views.BlogPageView.as_view(), name="blog"),
    # Posts
    path('post/add', views.addPostView.as_view(), name="add_post"),
    path('post/<int:pk>/update', views.updatePostView.as_view(), name="update_post"),
    path('post/<int:pk>', views.postDetailView.as_view(), name="post_detail"),
    path('post/<int:pk>/like', views.likeView, name="like_post"),
    # Comments
    path('add-comment/<int:post_id>/', views.add_comment, name="add_comment"),
    # Categories
    path('categoria/<int:categoria_id>/', views.ver_categoria, name="ver_categoria_post"),
]