# Generated by Django 4.0.1 on 2022-03-15 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0024_alter_publisherneeds_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisherneeds',
            name='is_accepted',
            field=models.BooleanField(blank=True, choices=[(True, 'نعم'), (False, 'لا')], default=False, null=True),
        ),
    ]
