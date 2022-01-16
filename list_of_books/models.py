from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    published_date = models.CharField(max_length=20, null=True, blank=True)
    ISBN_number = models.IntegerField(null=True, blank=True)
    page_count = models.IntegerField(null=True, blank=True)
    thumbnail = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return f'{self.authors} - {self.title}'
