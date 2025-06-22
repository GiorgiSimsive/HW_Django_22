from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password', 'password_confirm', 'avatar', 'phone_number', 'country']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("password_confirm"):
            self.add_error("password_confirm", "Пароли не совпадают")
        return cleaned_data


class EmailAuthForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput())
