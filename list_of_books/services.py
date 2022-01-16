import requests


def get_books(q_search, terms=None, term_search=None):
    if terms and term_search:
        url = f'https://www.googleapis.com/books/v1/volumes?q={q_search}+{terms}:{term_search}'
    else:
        url = f'https://www.googleapis.com/books/v1/volumes?q={q_search}'
    req = requests.get(url).json()
    books = req['items']
    return books
