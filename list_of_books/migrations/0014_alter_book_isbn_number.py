# Generated by Django 4.0.1 on 2022-01-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_of_books', '0013_alter_book_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
