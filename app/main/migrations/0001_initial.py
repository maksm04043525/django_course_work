# Generated by Django 5.1.3 on 2024-11-12 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='полное имя')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('gender', models.CharField(max_length=25, verbose_name='Пол')),
                ('nationality', models.CharField(max_length=50, verbose_name='национальность')),
                ('bio', models.TextField(verbose_name='биография')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='actors_photos/', verbose_name='фото')),
            ],
            options={
                'verbose_name': 'Актёр',
                'verbose_name_plural': 'Актёры',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='название фильма')),
                ('release_year', models.IntegerField(verbose_name='год премьеры')),
                ('budget', models.IntegerField(verbose_name='бюджет')),
                ('fees', models.IntegerField(verbose_name='сборы')),
                ('descr', models.TextField(verbose_name='описание фильма')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='film_posters/', verbose_name='постер')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=30, verbose_name='жанр')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='ActorFilm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.actor')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.film')),
            ],
            options={
                'verbose_name': 'Фильм актёра',
                'verbose_name_plural': 'Фильмы актёров',
                'unique_together': {('actor', 'film')},
            },
        ),
        migrations.CreateModel(
            name='FilmGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.film')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.genre')),
            ],
            options={
                'verbose_name': 'Жанр фильма',
                'verbose_name_plural': 'Жанры фильмов',
                'unique_together': {('film', 'genre')},
            },
        ),
    ]
