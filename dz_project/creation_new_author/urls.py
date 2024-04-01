from django.urls import path

from . import views

app_name = "creation_new_author"

urlpatterns = [
    path('create_author/', views.create_author, name='create_author'),
    path('add_quote/', views.add_quote, name='add_quote'),


]
