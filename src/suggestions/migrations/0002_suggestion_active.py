# Generated by Django 5.0.6 on 2024-05-29 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
