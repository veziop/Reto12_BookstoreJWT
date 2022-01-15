# Generated by Django 4.0.1 on 2022-01-15 22:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api_bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]