# Generated by Django 4.0.1 on 2022-01-17 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_of_books', '0021_alter_book_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='thumbnail',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
