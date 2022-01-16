from django.test import TestCase
from django.urls import reverse

from list_of_books.models import Book


class TestModels(TestCase):

    def setUp(self):
        self.book = Book.objects.create(title='some book',
                                        authors='some author',
                                        published_date='1999-01-01',
                                        ISBN_number='1596578524',
                                        page_count=123,
                                        thumbnail='None',
                                        language='pl')

    def test_book_is_assigned_id_on_creation(self):
        self.assertEquals(self.book.id, 5)

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.book.title, str)
        self.assertIsInstance(self.book.authors, str)
        self.assertIsInstance(self.book.published_date, str)
        self.assertIsInstance(self.book.ISBN_number, str)
        self.assertIsInstance(self.book.page_count, int)
        self.assertIsInstance(self.book.thumbnail, str)
        self.assertIsInstance(self.book.language, str)
