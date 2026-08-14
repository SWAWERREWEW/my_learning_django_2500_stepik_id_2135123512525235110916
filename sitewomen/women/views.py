# sitewomen\women\views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from .models import Women, Category, TagPost, UploadFiles
from .forms import AddPostForm, UploadFileForm
from .utils import DataMixin, menu

from django.core.paginator import Paginator
from gc import get_objects
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify


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


@login_required
def about(request):
    contact_list = Women.published.all()
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'women/about.html',
        {'title': 'О сайте 🔍', 'menu': menu, 'page_object': page_object})


class ShowPost(DataMixin, DetailView):
    context_object_name = 'post'
    template_name = 'women/post.html'
    slug_url_kwargs = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwargs])


def contact(request):
    return render(request,'women/contact.html',{'title': '📶Контакты🛠', 'menu': menu})


def login(request):
    return HttpResponse(f"Авторизация 🗝")


class WomenCategory(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.published.filter(cat__slug=self.kwargs['cat_slug']).select_related("cat")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        return self.get_mixin_context(context, title='Категория - ' + cat.name, cat_selected=cat.pk)


def custom_page_not_found(request, exception):
    return HttpResponseNotFound("<h1> Страница не найдена </h1>")


class TagPostList(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        return self.get_mixin_context(context, title='Тег: ' + tag.tag)
        # context['title'] = 'Тег: ' + tag.tag
        # context['menu'] = menu
        # context['cat_selected'] = None
        # return context

    def get_queryset(self):
        return Women.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')


class EditPage(DataMixin, UpdateView):
    model = Women
    fields = "__all__"
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    title_page = "Редактирование статьи 🛠"


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    title_page = 'Добавление статьи➕'

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class WomenHome(DataMixin, ListView):
    # # По умолчанию ищется шаблон \women\women\women_list.html но у нас такого нету❌📁⚠
    template_name = 'women/index.html'
    cat_selected = 0
    context_object_name = "posts"
    title_page = 'главная страница 🏠'

    def get_queryset(self):
        return Women.published.all().select_related('cat')
