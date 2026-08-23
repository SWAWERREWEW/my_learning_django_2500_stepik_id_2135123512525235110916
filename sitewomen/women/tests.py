# sitewomen\women\tests.py
from django.test import TestCase
from django.urls.base import reverse
from http import HTTPStatus
from women.models import Women


# Create your tests here.
class GetPagesTestCase(TestCase):
    fixtures = ['db.json']

    def setUp(self):
        "Инициализация перед выполнением каждого теста"

    def test_admin(self):
        path = reverse('admin:index')
        response = self.client.get(path)
        print('🛠🔍📊Созданный тест админ панели', response)

    def test_addpage(self):
        path = reverse('add_page')
        response = self.client.get(path)
        print('🛠🔍📊Созданный тест редактирования статьи', response)

    def test_redirect_addpage(self):
        path = reverse('add_page')
        redirect_uri = reverse('users:login') + '?next=' + path
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, redirect_uri)

    def test_mainpage(self):
        path = reverse('home')
        response = self.client.get(path)
        print('🛠🔍📊Созданный тест', response)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'women/index.html')
        self.assertEqual(response.context_data['title'], 'главная страница 🏠')
        # self.assertIn('women/base.html', response.template_name)

    def test_data_mainpage(self):
        women_posts_cache = Women.published.all().select_related('cat')
        path = reverse('home')
        response = self.client.get(path)
        print(women_posts_cache, response)
        self.assertQuerysetEqual(response.context_data['posts'], women_posts_cache)
        # self.assertQuerysetEqual(response.context_data['posts'], women_posts_cache[:5])

    def test_paginate_mainpage(self):
        path = reverse('home')
        page = 1
        paginate_by = 5
        response = self.client.get(path + f'?page={page}')
        w = Women.published.all().select_related('cat')
        self.assertQuerysetEqual(response.context_data['posts'], w[(page - 1) * paginate_by:page * paginate_by])

    def test_content_post(self):
        w = Women.published.get(pk=1)
        path = reverse('post', args=[w.slug])
        # path = reverse('post', args=['70day'])
        response = self.client.get(path)
        self.assertEqual(w.content, response.context_data['post'].content)

    def tearDown(self):
        "Действия после выполнения каждого теста"
