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
