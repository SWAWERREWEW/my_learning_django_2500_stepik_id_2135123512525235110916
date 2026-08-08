# sitewomen\women\views.py
from django.urls.base import reverse_lazy
from .models import Women, Category, TagPost, UploadFiles
from .forms import AddPostForm, UploadFileForm

from gc import get_objects
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
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
    posts = Women.published.all().select_related('cat')
    data = {
        'title': 'главная страница 🏠',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, "women/index.html", context=data)


# def handle_uploaded_file(f):
#     with open(f"sitewomen/uploads/{f.name}", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def about(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
            # Передаётся атрибут из класса UploadFileForm
            # handle_uploaded_file(form.cleaned_data['file'])
        # handle_uploaded_file(request.FILES["file_upload"])
    else:
        form = UploadFileForm()
    return render(request, 'women/about.html',
        {'title': 'О сайте 🔍', 'menu': menu, 'form': form})


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }

    return render(request, 'women/post.html', data)


class ShowPost(DetailView):
    context_object_name = 'post'
    template_name = 'women/post.html'
    slug_url_kwargs = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post'].title
        context['menu'] = menu
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwargs])


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            print("ЛоЛ")
            print(form.cleaned_data)
            form.save()
            # try:
                # print([i for i in form.cleaned_data.keys()])
                # print([i for i in form.cleaned_data.values()])
                # print(*form.cleaned_data)
                # Women.objects.create(**form.cleaned_data)
                # print("Ура, победа✅📥💾📦")
                # print(form.add_error(None, "Ура, победа, всё отправлено 💾📦📥✅ создана запись" +
                #                      str([i for i in form.cleaned_data.values()])))
            # except:
            #     print(form.add_error(None, "Неизвестная ошибка при записи в базу данных"))

    else:
        form = AddPostForm()

    data = {
        'menu': menu,
        'title': 'Добавить статью➕',
        'form': form
    }
    return render(request, 'women/addpage.html', data)


def contact(request):
    return HttpResponse(f"Обратная связь 💬")


def login(request):
    return HttpResponse(f"Авторизация 🗝")


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk).select_related("cat")
    data = {
        'title': f'Рубрика {category.name} 📊',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, "women/index.html", context=data)


class WomenCategory(ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.published.filter(cat__slug=self.kwargs['cat_slug']).select_related("cat")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        context['title'] = 'Категория - ' + cat.name
        context['menu'] = menu
        context['cat_selected'] = cat.pk
        return context


def custom_page_not_found(request, exception):
    return HttpResponseNotFound("<h1> Страница не найдена </h1>")


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related("cat")
    data = {
        'title': f"Тег: {tag.tag}",
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }
    return render(request, 'women/index.html', context=data)


class TagPostList(ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        context['title'] = 'Тег: ' + tag.tag
        context['menu'] = menu
        context['cat_selected'] = None
        return context

    def get_queryset(self):
        return Women.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')


class EditPage(UpdateView):
    model = Women
    fields = "__all__"
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    extra_context = {
        "menu": menu,
        "title": "Редактирование статьи 🛠"
    }


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    # success_url = reverse_lazy('home')
    extra_context = {
        'menu': menu,
        'title': 'Добавление статьи➕'
    }
    # def form_valid(self, form):
    #     form.save()
    #     super().form_valid(form)

# class AddPage(View):
#     def get(self, request):
#         form = AddPostForm(request.POST, request.FILES)
#         data = {
#             'menu': menu,
#             'title': 'Добавить статью➕',
#             'form': form
#         }
#         return render(request, 'women/addpage.html', data)
#     def post(self, request):
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             print("ЛоЛ")
#             print(form.cleaned_data)
#             form.save()
#         data = {
#             'menu': menu,
#             'title': 'Добавить статью➕',
#             'form': form
#         }
#         return render(request, 'women/addpage.html', data)


class WomenHome(ListView):
    # model = Women
    # По умолчанию ищется шаблон \women\women\women_list.html но у нас такого нету❌📁⚠
    template_name = 'women/index.html'
    context_object_name = "posts"
    extra_context = {
        'title': 'главная страница 🏠',
        'menu': menu,
        'cat_selected': 0,
    }

    def get_queryset(self):
        return Women.published.all().select_related('cat')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["title"] = 'главная страница 🏠'
    #     context["menu"] = menu
    #     context["posts"] = Women.published.all().select_related('cat')
    #     context["cat_selected"] = int(self.request.GET.get("cat_id", 0))
    #     return context
