from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('tag/<int:tag_id>/', views.tag_detail, name='tag_detail'),
    path('author/<int:author_id>', views.author_detail, name='author_detail')
]
