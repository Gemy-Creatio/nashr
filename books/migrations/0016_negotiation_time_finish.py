# Generated by Django 4.0.1 on 2022-03-13 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_bookdistrubuting_user_negotiation'),
    ]

    operations = [
        migrations.AddField(
            model_name='negotiation',
            name='time_finish',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
