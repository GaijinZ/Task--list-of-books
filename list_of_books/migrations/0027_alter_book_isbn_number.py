# Generated by Django 4.0.1 on 2022-01-18 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_of_books', '0026_alter_book_isbn_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN_number',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
