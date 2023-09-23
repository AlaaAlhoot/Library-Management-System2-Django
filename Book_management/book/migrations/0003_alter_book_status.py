# Generated by Django 4.2.1 on 2023-09-21 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_book_photo_author_author_photo_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(blank=True, choices=[('available', 'Available'), ('sold', 'Sold'), ('rented', 'Rented')], max_length=50, null=True),
        ),
    ]