from django.urls import path
from .views import register_view, CustomLoginView
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
]
