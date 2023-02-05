# Generated by Django 4.1.2 on 2023-02-05 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_rename_movies_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating_avg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='rating_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='rating_last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
