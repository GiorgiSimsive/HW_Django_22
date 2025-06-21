from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from users.forms import RegisterForm, EmailAuthForm


def home_view(request):
    return HttpResponse("Добро пожаловать на главную страницу!")


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)

            send_mail(
                subject='Добро пожаловать!',
                message=f'Привет, {user.email}!\nСпасибо за регистрацию.',
                from_email=None,
                recipient_list=[user.email],
                fail_silently=False,
            )

            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    authentication_form = EmailAuthForm
