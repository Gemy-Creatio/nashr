# Generated by Django 4.0.1 on 2022-03-19 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0003_printbookrequest_paper_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printbookrequest',
            name='book',
            field=models.FileField(blank=True, null=True, upload_to='books_print/'),
        ),
    ]
