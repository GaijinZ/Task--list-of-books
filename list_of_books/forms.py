from datetime import datetime
from string import ascii_letters
from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    published_date = forms.DateField(label='Published Date (Year-Month-Day)', input_formats=['%Y-%m-%d'],
                                     widget=forms.DateTimeInput(format='%Y-%m-%d'))

    def clean_authors(self):
        authors = self.cleaned_data['authors']
        if authors.isdigit():
            raise forms.ValidationError('Authors field accept letters only.')
        return authors

    def clean_ISBN_number(self):
        isbn = self.cleaned_data['ISBN_number']
        if isbn is not None and Book.objects.filter(ISBN_number=isbn).exists():
            raise forms.ValidationError(f"The book's ISBN {isbn} already exists.")
        return isbn

    def clean_language(self):
        language = self.cleaned_data['language']
        if language is not None and not language.isalpha() and language not in ascii_letters:
            raise forms.ValidationError('Language field accept letters only'
                                        ' with no special characters.')
        return language

    def clean_published_date(self):
        published_date = self.cleaned_data['published_date']

        if published_date > datetime.now().date():
            raise forms.ValidationError('Published date cannot be later than today.')
        return str(published_date)

    class Meta:
        model = Book
        fields = '__all__'
