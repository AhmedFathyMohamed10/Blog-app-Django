from django.urls import path
from . import views

urlpatterns = [
    path("home", views.index, name="index"),
    path("about", views.about, name="about"),
    path("post/<str:post_id>", views.post, name="post"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("comment/<str:post_id>", views.comment_on_post, name="comment"),
]