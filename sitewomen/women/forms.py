# sitewomen\women\forms.py
from django import forms
from django.utils.deconstruct import deconstructible
from .models import Husband, Category, Women
from django.core.validators import MinLengthValidator, MaxLengthValidator, ValidationError


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


"""
class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=3, label="🔳Зугаловок", error_messages={
    'min_length': 'БОЛЬШЕ БУКАВ',
    'required': 'СУПЕР НУЖНОЕ ПОЛЕ'})
    # title = forms.CharField(max_length=255, min_length=3, label="🔳Зугаловок", error_messages={
    # 'min_length': 'БОЛЬШЕ БУКАВ',
    # 'required': 'СУПЕР НУЖНОЕ ПОЛЕ'}, validators=[RussianValidator(),])
    slug = forms.SlugField(max_length=300, label="🔳Слаг")
    # slug = forms.SlugField(max_length=300, label="🔳Слаг", validators=[
    #     MinLengthValidator(5),
    #     MaxLengthValidator(100)])
    content = forms.CharField(widget=forms.Textarea(attrs={"cols": 50, "rows": 3}), required=False,
        label="🔳КАНТЕНТсодержимое")
    is_published = forms.BooleanField(required=False, initial=True, label="🔳Публикованность")
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Что❓", label="🔳Котигорька")
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, empty_label="Что❓", label="🔳мУж")

    def clean_title(self):
        title = self.cleaned_data['title']
        ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "
        if not (set(title) <= set(ALLOWED_CHARS)):
            raise ValidationError("РОССИЯ СВЯЩЕННАЯ НАША ДЕРЖВА, РОССИЯ ОЧЕНЬ ЛЮБИТ РУССКИЕ СЛОВА")
        return title
"""
