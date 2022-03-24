# Generated by Django 4.0.1 on 2022-03-23 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0024_personwork'),
    ]

    operations = [
        migrations.AddField(
            model_name='personwork',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='personwork',
            name='rate',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='personwork',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
