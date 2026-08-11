# sitewomen/users/forms.py
from django import forms

class LoginUserForm(forms.Form):
    username = forms.CharField(label="🏠Погин", widget=forms.TextInput(attrs={"class": "form-input"}))
    password = forms.CharField(label="🗝Ларопь", widget=forms.PasswordInput(attrs={"class": "form-input"}))
