# Generated by Django 4.0.1 on 2022-03-23 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('designs', '0004_alter_printbookrequest_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookFormating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('book_size', models.CharField(blank=True, max_length=255, null=True)),
                ('book_color', models.CharField(blank=True, max_length=255, null=True)),
                ('font_type', models.CharField(blank=True, max_length=255, null=True)),
                ('font_size', models.CharField(blank=True, max_length=255, null=True)),
                ('drafts', models.CharField(blank=True, max_length=255, null=True)),
                ('main_address', models.CharField(blank=True, max_length=255, null=True)),
                ('main_font_type', models.CharField(blank=True, max_length=255, null=True)),
                ('main_font_size', models.CharField(blank=True, max_length=255, null=True)),
                ('main_font_color', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_address', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_font_type', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_font_size', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_font_color', models.CharField(blank=True, max_length=255, null=True)),
                ('double_address', models.CharField(blank=True, max_length=255, null=True)),
                ('book_intro', models.CharField(blank=True, max_length=255, null=True)),
                ('ehda_page', models.CharField(blank=True, max_length=255, null=True)),
                ('thank_page', models.CharField(blank=True, max_length=255, null=True)),
                ('define_page', models.CharField(blank=True, max_length=255, null=True)),
                ('intro_page', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('book_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
