from django.test import SimpleTestCase
from django.urls import reverse, resolve

from list_of_books.views import HomeView, \
                                AddEditBookView, \
                                SearchBookView, \
                                DeleteBook, \
                                ImportToDBView


class TestUrls(SimpleTestCase):

    def test_home_url_resolve(self):
        url = reverse('books:home')
        self.assertEqual(resolve(url).func.view_class, HomeView)

    def test_add_book_url_resolve(self):
        url = reverse('books:add-book')
        self.assertEqual(resolve(url).func.view_class, AddEditBookView)

    def test_edit_book_url_resolve(self):
        url = reverse('books:edit-book', args=['1'])
        self.assertEqual(resolve(url).func.view_class, AddEditBookView)

    def test_search_book_url_resolve(self):
        url = reverse('books:search-book')
        self.assertEqual(resolve(url).func.view_class, SearchBookView)

    def test_delete_book_url_resolve(self):
        url = reverse('books:delete-book', args=['1'])
        self.assertEqual(resolve(url).func.view_class, DeleteBook)

    def test_import_url_resolve(self):
        url = reverse('books:import')
        self.assertEqual(resolve(url).func.view_class, ImportToDBView)
