# Generated by Django 4.1.5 on 2023-01-26 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='prodimg',
            field=models.ImageField(null=True, upload_to='productimg'),
        ),
    ]
