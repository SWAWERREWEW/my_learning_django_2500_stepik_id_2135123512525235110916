# sitewomen/users/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="🏠Погин", widget=forms.TextInput(attrs={"class": "form-input"}))
    password = forms.CharField(label="🗝Ларопь", widget=forms.PasswordInput(attrs={"class": "form-input"}))

    class Meta:
        model = get_user_model()
        fields = ["username", "password"]

class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label="🏠Погин")
    password = forms.CharField(label="🗝Ларопь", widget=forms.PasswordInput())
    password2 = forms.CharField(label="🗝Снова Ларопь", widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name", "password", "password2"]
        labels = {
            "email": "📦Почта",
            "first_name": "📐Имечко",
            "last_name": "🍀Фамилия"
        }

    # Проверка паролей
    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("❌⚠🗝Пароли без совпадения🗝⚠❌")
        return cd["password"]

    # Проверка уникальности передаваемых почт
    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
             raise forms.ValidationError("⚠🏠🔍Обнаружена зарегистрированная почта🔍🏠⚠")
        return email
