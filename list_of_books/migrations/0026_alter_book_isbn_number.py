# Generated by Django 4.0.1 on 2022-01-18 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_of_books', '0025_alter_book_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN_number',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
