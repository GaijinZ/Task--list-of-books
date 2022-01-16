from django.test import TestCase, Client
from django.urls import reverse

from list_of_books.forms import BookForm
from list_of_books.models import Book


class TestForms(TestCase):
    def setUp(self):
        self.client = Client()
        self.book = Book.objects.create(title='some book',
                                        authors='some author',
                                        published_date='1999-01-01',
                                        ISBN_number=1596578524,
                                        page_count=123,
                                        thumbnail='None',
                                        language='pl')
        self.book.save()

    def test_book_form_valid_data(self):
        form = BookForm(data={
            'title': 'book title',
            'authors': 'book author',
            'published_date': '1995-05-05',
            'ISBN_number': 157856114,
            'page_count': 155,
            'thumbnail': 'None',
            'language': 'en'
        })

        self.assertTrue(form.is_valid())

    def test_book_form_no_data(self):
        form = BookForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_book_form_invalid_data(self):
        form = BookForm(data={
            'title': 'book title',
            'authors': 'book author',
            'published_date': '1995',
            'ISBN_number': 157856114,
            'page_count': 159,
            'thumbnail': 'None',
            'language': 'en2'
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_edit_form(self):
        get_book = Book.objects.get(title='some book')
        response = self.client.post(
            reverse(
                'books:edit-book', kwargs={'id': get_book.id}),
            {
                'title': 'The Catcher in the Rye',
                'author': 'book author',
                'published_date': '1999-01-01',
                'ISBN_number': 1596578524,
                'page_count': 123,
                'thumbnail': 'None',
                'language': 'en'
            }
        )

        self.assertEqual(response.status_code, 200)

        get_book.refresh_from_db()
        self.assertEqual(get_book.title, 'The Catcher in the Rye')
