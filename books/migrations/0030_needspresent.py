# Generated by Django 4.0.1 on 2022-03-19 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0029_advertisepresent'),
    ]

    operations = [
        migrations.CreateModel(
            name='NeedsPresent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('needs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.publisherneeds')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
