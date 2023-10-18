# Generated by Django 4.2.6 on 2023-10-18 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.AlterModelOptions(
            name='tipoatuacao',
            options={'verbose_name_plural': 'Tipos de Atuacao'},
        ),
    ]