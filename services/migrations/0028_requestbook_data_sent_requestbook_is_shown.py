# Generated by Django 4.0.1 on 2022-04-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0027_requestbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestbook',
            name='data_sent',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='requestbook',
            name='is_shown',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
