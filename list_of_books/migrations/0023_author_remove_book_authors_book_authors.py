# Generated by Django 4.0.1 on 2022-01-17 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_of_books', '0022_alter_book_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='list_of_books.Author'),
        ),
    ]
