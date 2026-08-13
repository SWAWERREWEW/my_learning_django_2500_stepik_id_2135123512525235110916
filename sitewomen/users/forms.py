# sitewomen/users/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="🏠Погин", widget=forms.TextInput(attrs={"class": "form-input"}))
    password = forms.CharField(label="🗝Ларопь", widget=forms.PasswordInput(attrs={"class": "form-input"}))

    class Meta:
        model = get_user_model()
        fields = ["username", "password"]

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="🏠Погин", widget=forms.TextInput(attrs={"class": "form-input"}))
    password1 = forms.CharField(label="🗝Ларопь", widget=forms.PasswordInput(attrs={"class": "form-input"}))
    password2 = forms.CharField(label="🗝Снова Ларопь", widget=forms.PasswordInput(attrs={"class": "form-input"}))

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
        labels = {
            "email": "📦Почта",
            "first_name": "📐Имечко",
            "last_name": "🍀Фамилия"
        }
        widgets = {
            "email": forms.TextInput(attrs={"class": "form-input"}),
            "first_name": forms.TextInput(attrs={"class": "form-input"}),
            "last_name": forms.TextInput(attrs={"class": "form-input"})
        }

    # Проверка уникальности передаваемых почт
    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
             raise forms.ValidationError("⚠🏠🔍Обнаружена зарегистрированная почта🔍🏠⚠")
        return email
