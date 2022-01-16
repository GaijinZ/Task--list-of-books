# Generated by Django 4.0.1 on 2022-01-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=200)),
                ('published_date', models.CharField(max_length=20)),
                ('ISBN_number_10', models.CharField(max_length=150)),
                ('ISBN_number_13', models.CharField(max_length=150)),
                ('page_count', models.IntegerField()),
                ('thumbnail', models.CharField(blank=True, max_length=255)),
                ('language', models.CharField(max_length=5)),
            ],
        ),
    ]
