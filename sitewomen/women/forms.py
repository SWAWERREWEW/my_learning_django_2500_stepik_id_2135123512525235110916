# sitewomen\women\forms.py
from django import forms
from django.utils.deconstruct import deconstructible
from .models import Husband, Category, Women
from django.core.validators import MinLengthValidator, MaxLengthValidator, ValidationError
from captcha.fields import CaptchaField

@deconstructible
class RussianValidator:
    ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else "РОССИЯ СВЯЩЕННАЯ НАША ДЕРЖВА, РОССИЯ ОЧЕНЬ ЛЮБИТ РУССКИЕ СЛОВА"

    def __call__(self, value):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code, params={"value": value})


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Что❓", label="🔳Котигорька")
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, empty_label="Что❓", label="🔳мУж")

    class Meta:
        model = Women
        # Импортированные поля
        fields = ['title', 'content', 'is_published', 'cat', 'husband', 'tags', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 3})
        }
        # Названия полей
        labels = {'title': 'НеЗугаловах'}

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError("51 символов блин много💥")
        return title


class UploadFileForm(forms.Form):
    file = forms.ImageField(label="Файл")


class ContactForm(forms.Form):
    name = forms.CharField(label='🔳Имя', max_length=255)
    email = forms.EmailField(label='📦Почта')
    content = forms.CharField(label='📝Содержимое', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField(label='💥💣🔥ЗАЩИТА_ОТ_ТРАНСФОРМЕРОВ🔥💣💥')
