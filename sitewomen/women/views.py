# sitewomen/women/views
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = [
    {'title': "О сайте 🔍", 'url_name': "about"},
    {'title': "Добавить статью ➕", 'url_name': "add_page"},
    {'title': "Обратная связь 💬", 'url_name': "contact"},
    {'title': "Войти 🚪", 'url_name': "login"}
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелина Джоли начинается с далёких 1700 годов,' +
    ' когда мы не знали, что происходит в мире и когда мы интересовались этой личностью, у нас закардывалась мысль о' +
    ' том, что мы делаем всё неправильно и некрасиво, потому что мы забили зонтик', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]


def index(request):
    data = {
        'title': 'главная страница 🏠',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, "women/index.html", context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте 🔍', 'menu': menu})


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id} 📝")


def addpage(request):
    return HttpResponse(f"Добавить статью ➕")


def contact(request):
    return HttpResponse(f"Обратная связь 💬")


def login(request):
    return HttpResponse(f"Авторизация 🗝")


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам 📊',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id
    }
    return render(request, "women/index.html", context=data)


def custom_page_not_found(request, exception):
    return HttpResponseNotFound("<h1> Страница не найдена </h1>")
