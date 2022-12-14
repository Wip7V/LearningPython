# Generated by Django 4.1 on 2022-08-28 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre completo del autor', max_length=150)),
                ('day_of_birth', models.DateField(blank=True, null=True)),
                ('day_of_death', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Nombre de la película', max_length=150)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(help_text='Descripción de la película', null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='film.author')),
            ],
        ),
    ]
