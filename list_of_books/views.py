from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, FormView, TemplateView, DeleteView

from .models import Book
from .forms import BookForm

from .services import get_books


class HomeView(ListView):
    template_name = 'books/books.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_books = Book.objects.all()

        context['all_books'] = all_books
        return context


class AddEditBookView(FormView):
    model = Book
    form_class = BookForm
    template_name = 'books/add-book.html'

    def post(self, request, id=None, *args, **kwargs):
        if id:
            book = get_object_or_404(Book, pk=id)
        else:
            book = None
        form = BookForm(request.POST, instance=book)
        if request.POST and form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {
            'form': form
        })


class SearchBookView(ListView):
    template_name = 'books/search-book.html'
    model = Book

    def get_dates_searched(self):
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        results = Book.objects.filter(published_date__range=(date_from, date_to))
        return results

    def get_lang_title_author_searched(self):
        query = self.request.GET.get('q')
        if len(query) <= 2:
            lookups = Q(language__iexact=query)
        else:
            lookups = Q(title__icontains=query) | Q(authors__icontains=query)
        results = Book.objects.filter(lookups).distinct()
        return results

    def get(self, *args, **kwargs):
        submit_button = self.request.GET.get('submit')
        if self.request.GET.get('date_from') and self.request.GET.get('date_to'):
            results = self.get_dates_searched()
        elif self.request.GET.get('q'):
            results = self.get_lang_title_author_searched()
        else:
            return render(self.request, 'books/search-book.html', {
                'submit_button': submit_button
            })
        context = {
            'results': results,
            'submit_button': submit_button
        }
        return render(self.request, 'books/search-book.html', context)


class RedirectToPreviousMixin:
    default_redirect = '/'

    def get(self, request, *args, **kwargs):
        request.session['previous_page'] = request.META.get('HTTP_REFERER', self.default_redirect)
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.session['previous_page']


class DeleteBook(RedirectToPreviousMixin, DeleteView):
    model = Book
    template_name = 'books/delete-book.html'


class ImportToDBView(TemplateView):
    template_name = 'books/import.html'
    model = Book

    def get_queryset(self):
        return Book.objects.all()

    def get_books_from_api(self):
        q_search = self.request.POST.get('q_search')
        if self.request.POST.get('terms') and self.request.POST.get('term_search'):
            terms = self.request.POST.get('terms')
            term_search = self.request.POST.get('term_search')
            return get_books(q_search, terms, term_search)
        return get_books(q_search)

    @staticmethod
    def save_books_into_model(books):
        for book in books:
            check_isbn_type = ''

            if book['volumeInfo']['industryIdentifiers'][0]['type'] == 'OTHER':
                check_isbn_type += \
                    book['volumeInfo']['industryIdentifiers'][0]['identifier'].split(':')[1]
            else:
                get_isbn_13 = \
                    [isbn_13 for isbn_13 in
                     book['volumeInfo']['industryIdentifiers'] if isbn_13['type'] == 'ISBN_13']
                check_isbn_type += get_isbn_13[0]['identifier']

            Book.objects.update_or_create(title=book['volumeInfo']['title'],
                                          authors=', '.join([i for i in book['volumeInfo']
                                                                            ['authors']])
                                          if 'authors' in book['volumeInfo']
                                          else 'Unknown',
                                          published_date=book['volumeInfo']['publishedDate'],
                                          ISBN_number=int(check_isbn_type),
                                          page_count=book['volumeInfo']['pageCount']
                                          if 'pageCount' in book['volumeInfo']
                                          else 0,
                                          thumbnail=book['volumeInfo']
                                          .get('imageLinks')['thumbnail']
                                          if 'imageLinks' in book['volumeInfo']
                                          else 'https://code-artisan.io/wp-content/uploads/2020/12'
                                               '/default_book_cover_2015.jpg',
                                          language=book['volumeInfo']['language']
                                          )

    def post(self, *args, **kwargs):
        if self.request.POST.get('q_search') != '':
            books = self.get_books_from_api()
            self.save_books_into_model(books)
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/')
