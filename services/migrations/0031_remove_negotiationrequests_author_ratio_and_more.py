# Generated by Django 4.0.1 on 2022-04-17 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0030_negotiationrequests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='negotiationrequests',
            name='author_ratio',
        ),
        migrations.RemoveField(
            model_name='negotiationrequests',
            name='author_rights',
        ),
        migrations.RemoveField(
            model_name='negotiationrequests',
            name='number_of_copies',
        ),
        migrations.RemoveField(
            model_name='negotiationrequests',
            name='price',
        ),
        migrations.RemoveField(
            model_name='negotiationrequests',
            name='time_finish',
        ),
        migrations.AlterField(
            model_name='negotiationrequests',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
