from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Genre(models.Model):
    genre_name = models.CharField('жанр', max_length=30, unique=True)

    def __str__(self):
        return self.genre_name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Actor(models.Model):
    name = models.CharField('полное имя', max_length=100)
    birth_date = models.DateField('Дата рождения')
    gender = models.CharField('Пол', max_length=25)
    bio = models.TextField('биография')
    photo = models.ImageField('фото', upload_to='actors_photos/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актёр'
        verbose_name_plural = 'Актёры'


class Film(models.Model):
    title = models.CharField('название фильма', max_length=250)
    rating = models.FloatField('рейтинг', validators=[MinValueValidator(0), MaxValueValidator(10)],blank=True,null=True)
    release_year = models.IntegerField('год премьеры')
    budget = models.IntegerField('бюджет')
    fees = models.IntegerField('сборы')
    descr = models.TextField('описание фильма')
    poster = models.ImageField('постер', upload_to='film_posters/', blank=True, null=True)
    trailer_url = models.URLField('трейлер', max_length=500, blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name='films')
    actors = models.ManyToManyField(Actor,related_name='films',verbose_name='Актёры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'



class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    descr = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='announcements/', blank=True, null=True, verbose_name="Изображение")
    date = models.DateField(verbose_name="Дата анонса")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"



class Comment(models.Model):
    film = models.ForeignKey('Film', on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=100,verbose_name="имя пользователя")
    rating = models.FloatField('рейтинг', validators=[MinValueValidator(0), MaxValueValidator(10)],blank=True,null=True)
    text = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.username} - {self.film.title}"

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"
