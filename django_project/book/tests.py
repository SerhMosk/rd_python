from django.contrib.auth import get_user_model
from django.test import TestCase

from book.models import Book


class TestBookModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        # cls.user = get_user_model().objects.create(username='test_user', password='test_password')
        cls.book = Book.objects.create(title='Test title', author='Test Author', year=2022, price=100)

    def test_model_data(self):
        self.assertEqual(self.book.title, 'Test title')
        self.assertEqual(self.book.author, 'Test Author')
        self.assertEqual(self.book.year, 2022)
        self.assertEqual(self.book.price, 100)

    def test_book_list_view(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/book_list.html')
        self.assertContains(response, 'Book List')

    def test_book_detail_view(self):
        response = self.client.get(f'/books/{self.book.pk}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/book_detail.html')
        self.assertContains(response, 'Book Detail')
        self.assertContains(response, 'Test title')

    def test_book_create_view(self):
        response = self.client.post('/books/create', {
            'title': 'Test title 1',
            'author': 'Test Author',
            'year': 2023,
            'price': 1000
        })
        self.assertEqual(response.status_code, 302)

    def test_book_update_view(self):
        response = self.client.post(f'/books/{self.book.pk}/update', {
            'title': 'Test title 2',
            'author': 'Test Author',
            'year': 2023,
            'price': 100
        })
        self.assertEqual(response.status_code, 302)

    def test_book_delete_view(self):
        response = self.client.post(f'/books/{self.book.pk}/delete')
        self.assertEqual(response.status_code, 302)

    def test_get_absolute_url(self):
        self.assertEqual(self.book.get_absolute_url(), '/books/1')
