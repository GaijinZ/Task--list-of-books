import requests


def get_books(q_search, terms=None, term_search=None):
    url = f'https://www.googleapis.com/books/v1/volumes?q={q_search}'
    if terms and term_search:
        url = url + f'+{terms}:{term_search}'
    req = requests.get(url).json()
    books = req['items']
    return books
