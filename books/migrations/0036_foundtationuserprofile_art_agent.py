# Generated by Django 4.0.1 on 2022-03-23 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0035_negotiation_is_accepted_negotiationbook_is_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='foundtationuserprofile',
            name='art_agent',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
