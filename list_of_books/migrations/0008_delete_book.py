# Generated by Django 4.0.1 on 2022-01-13 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list_of_books', '0007_alter_book_page_count'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
