# Generated by Django 4.0.1 on 2022-03-23 18:22

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0006_alter_bookformating_book_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookformating',
            name='book_file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name=books.models.Book),
        ),
    ]
