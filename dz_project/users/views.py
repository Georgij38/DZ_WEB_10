from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            birth_date = form.cleaned_data.get('birth_date')
            Profile.objects.create(user=user, birth_date=birth_date)
            login(request, user)
            return redirect('users:login')  # Перевірте, чи правильно вказано URL для перенаправлення
    else:
        form = RegisterForm()
    return render(request, 'users/signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('account:profile')
            else:
                return render(request, 'users/login.html', {'form': form, 'error_message': 'Invalid login'})
    else:
        form = LoginForm()
    return render(request, 'users:login', {'form': form})


def logout_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')

        # Перевірка, чи користувач існує та чи пароль вірний
        user = User.objects.filter(username=username, email=email).first()
        if user and user.check_password(password):
            # Видалення користувача
            user.delete()
            # Вихід користувача з системи
            logout(request)
            messages.success(request, 'Your account has been deleted.')
            return redirect('users:signup')  # Замініть 'login' на URL для сторінки входу
        else:
            messages.error(request, 'Invalid username, email, or password.')

    return render(request, 'users/logout.html')


def profile_view(request):

    return redirect('quotes:root')
