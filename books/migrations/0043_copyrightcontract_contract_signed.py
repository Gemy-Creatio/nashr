# Generated by Django 4.0.1 on 2022-04-07 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0042_bookcontract_contract_signed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='copyrightcontract',
            name='contract_signed',
            field=models.FileField(blank=True, null=True, upload_to='contract-signed/'),
        ),
    ]
