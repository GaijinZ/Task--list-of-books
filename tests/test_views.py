from django.test import TestCase, Client
from django.urls import reverse

from list_of_books.models import Book


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.book = Book.objects.create(title='some book',
                                        authors='some author',
                                        published_date='1999-01-01',
                                        ISBN_number='1596578524',
                                        page_count=123,
                                        thumbnail='None',
                                        language='pl')
        self.book.save()

    def test_book_get(self):
        get_book = Book.objects.get(title='some book')

        self.assertEquals(get_book.title, 'some book')
