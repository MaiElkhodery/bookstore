# Generated by Django 5.0.2 on 2024-03-21 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='', max_length=150),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
