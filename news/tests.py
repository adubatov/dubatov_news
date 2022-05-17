from urllib import response
from django.urls import reverse
from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model, authenticate

from news.models import Article

# Create your tests here.
class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class SignupPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@me.com'

    def test_signup_page_status_code(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)


class NewsListTests(TestCase):
    def test_news_list_status_code(self):
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)

    def test_news_list_url_by_name(self):
        response = self.client.get(reverse('news_list'))
        return self.assertEqual(response.status_code, 200)

    def test_news_list_uses_correct_template(self):
        response = self.client.get(reverse('news_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news_list.html')


class NewsCreateTests(TestCase):
    def test_news_create_not_authenticated_status_code(self):
        response = self.client.get(f'/news/create/')
        self.assertEqual(response.status_code, 302)
