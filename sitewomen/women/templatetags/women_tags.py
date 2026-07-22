# sitewomen\women\templatetags\women_tags.py
from django import template
from women.views import cats_db

# Регистрация новых тегов
register = template.Library()

@register.simple_tag(name='g')
def get_categories():
    return cats_db

@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    cats = cats_db
    return {'cats': cats, 'cat_selected': cat_selected}