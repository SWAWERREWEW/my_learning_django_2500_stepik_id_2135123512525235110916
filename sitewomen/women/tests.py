# sitewomen\women\tests.py
from django.test import TestCase
from django.urls.base import reverse
from http import HTTPStatus

# Create your tests here.
class GetPagesTestCase(TestCase):
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

    def tearDown(self):
        "Действия после выполнения каждого теста"
