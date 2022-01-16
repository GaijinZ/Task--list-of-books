from django.urls import path

from .views import HomeView, AddEditBookView, SearchBookView, DeleteBook, ImportToDBView

app_name = 'books'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-book/', AddEditBookView.as_view(), name='add-book'),
    path('edit-book/<int:id>', AddEditBookView.as_view(), name='edit-book'),
    path('delete-book/<int:pk>', DeleteBook.as_view(), name='delete-book'),
    path('search-book/', SearchBookView.as_view(), name='search-book'),
    path('import/', ImportToDBView.as_view(), name='import'),
]
