# sitewomen\women\models.py
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from .my_dop_functions import cyrillic_to_latin


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


# Create your models here.
class Women(models.Model):
    class Meta:
        verbose_name = "Женщина с планеты кибертрон в классе мета"
        verbose_name_plural = "Женщины с планеты кибертрон в классе мета"

        ordering = ['time_create']
        indexes = [
            models.Index(fields=['time_create'])
        ]

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(cyrillic_to_latin(self.title))
        super().save(self, *args, **kwargs)


    objects = models.Manager()
    published = PublishedManager()
    title = models.CharField(max_length=255, verbose_name="зугаловах")
    slug = models.SlugField(max_length=300, unique=True, db_index=True, verbose_name="СЛагъ")
    content = models.TextField(blank=True, verbose_name="КАНТЕНТсодержимое")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Тайм рождения")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Обнова")
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
        default=Status.DRAFT, verbose_name="Стутус")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name="Котигория")
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags', verbose_name="Тегишки")
    husband = models.OneToOneField('Husband', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='wuman', verbose_name="Мужьяки")

class Category(models.Model):
    class Meta:
        verbose_name = "Категорька из категорий в классе Мета"
        verbose_name_plural = "Категорьки из категорий в классе Мета"

    name = models.CharField(max_length=100, db_index=True, verbose_name="ИменаНоНеймов")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="СЛагъ")
    # tags = models.ManyToManyField('Women', blank=True, related_name='Womans')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    some_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name


class AgainWomen(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
