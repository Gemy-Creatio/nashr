# Generated by Django 4.0.1 on 2022-04-09 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0025_personwork_end_date_personwork_rate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtitleservice',
            name='subtitle_type',
            field=models.CharField(blank=True, choices=[('دبلجة صوتية', 'دبلجة صوتية '), ('ترجمة شاشة', 'ترجمة شاشة')], max_length=255, null=True),
        ),
    ]
