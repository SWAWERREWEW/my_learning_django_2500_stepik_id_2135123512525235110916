# sitewomen\users\tests.py
from django.test import TestCase
from django.urls.base import reverse
from http import HTTPStatus
from django.contrib.auth import get_user_model


class RegisterUserTestCase(TestCase):

    def setUp(self):
        self.data_for_check = {
            'username': 'koshka',
            'email': 'koshka@sitewomen.ru',
            'first_name': 'koshka',
            'last_name': 'koshka',
            'password1': 'gugirufi',
            'password2': 'gugirufi',
        }

    def test_form_registration_get(self):
        path = reverse('users:register')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_user_registration_success(self):
        user_model = get_user_model()

        path = reverse('users:register')
        response = self.client.post(path, self.data_for_check)
        # Проверка на то, перешёл ли пользователь на переданный путь или его перенаправило на другой
        self.assertRedirects(response, reverse('users:login'))
        # Проверка на существование нового пользователя по уникальной почте
        self.assertTrue(user_model.objects.filter(username=self.data_for_check['username']).exists())
        # self.assertTrue(user_model.objects.filter(email=data_for_check['email']).exists())

    def test_user_registration_password_error(self):
        data_for_check = {
            'username': 'stone',
            'email': 'stone@sitewomen.ru',
            'first_name': 'stone',
            'last_name': 'stone',
            'password1': 'wetrter90g',
            'password2': '4mnpwoitire',
        }

        path = reverse('users:register')
        response = self.client.post(path, data_for_check)
        self.assertContains(response, "Введенные пароли не совпадают.", html=True)
        self.assertContains(response, "не", html=False)

    def test_user_registration_user_exists_error(self):
        user_model = get_user_model()
        user_model.objects.create(username=self.data_for_check['username'])

        path = reverse('users:register')
        response = self.client.post(path, self.data_for_check)
        self.assertContains(response, "уже существует", html=False)
