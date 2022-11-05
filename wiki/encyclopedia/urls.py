from django.urls import path

from . import views

# app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.title, name="title"),
    path("search/", views.search, name="search"),
    path("new/", views.new_page, name="new_pg"),
    path("edit/", views.edit_page_init, name="edit_page_init"),
    path("random/", views.random_page, name="random_page")
]
