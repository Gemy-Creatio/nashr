# Generated by Django 4.0.1 on 2022-02-23 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_designservice_filed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designservice',
            name='text_file',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='', verbose_name='Text File'),
        ),
    ]
