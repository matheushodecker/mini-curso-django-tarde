# Generated by Django 4.2.6 on 2023-10-18 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_filmes'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmes',
            name='categorias',
            field=models.ManyToManyField(to='core.categoria'),
        ),
    ]
