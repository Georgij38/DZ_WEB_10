from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "users"

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]
