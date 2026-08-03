# sitewomen\women\forms.py
from django import forms
from .models import Husband, Category

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label="🔳Зугаловок")
    slug = forms.SlugField(max_length=300, label="🔳Слаг")
    content = forms.CharField(widget=forms.Textarea(attrs={"cols": 50, "rows": 3}), required=False,
        label="🔳КАНТЕНТсодержимое")
    is_published = forms.BooleanField(required=False, initial=True, label="🔳Публикованность")
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Что❓", label="🔳Котигорька")
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, empty_label="Что❓", label="🔳мУж")
