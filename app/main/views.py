from django.shortcuts import render, get_object_or_404, redirect
from .models import Actor, Film, Genre, News
from .forms import CommentForm


def index(request):
    actrindex = Actor.objects.all()
    filmindex = Film.objects.all()
    return render(request, 'main/index.html',
                  context={'actor': actrindex, 'film': filmindex})


def actor_detail(request, actor_id):
    actor = get_object_or_404(Actor, id=actor_id)
    films= actor.films.all()
    return render(request, 'main/actor_detail.html',
                  context={'actor': actor,'films':films})



def film_detail(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    actors = film.actors.all()
    genres = film.genres.all()

    # Обработка комментариев
    comments = film.comments.order_by('-created_at')  # Получение всех комментариев к фильму
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Создаем комментарий, но не сохраняем сразу
            comment = form.save(commit=False)
            comment.film = film  # Привязываем комментарий к фильму
            comment.save()  # Сохраняем в базу данных
            return redirect('film_detail', film_id=film_id)  # Перенаправление на ту же страницу
    else:
        form = CommentForm()

    return render(request, 'main/film_detail.html', {
        'film': film,
        'actors': actors,
        'genres': genres,
        'comments': comments,
        'form': form
    })



def actor_list(request):
    actorlist = Actor.objects.all()
    return render(request, 'main/actor_list.html',
                  context={'actor':actorlist})



def film_filter(request):
    # Получаем список жанров из GET-параметров
    selected_genres = request.GET.getlist('genres')
    search_query = request.GET.get('search', '')

    # Начинаем с фильтрации всех фильмов
    films = Film.objects.all()

    # Фильтруем фильмы по жанрам, если жанры выбраны
    if selected_genres:
        selected_genres = [int(genre_id) for genre_id in selected_genres]
        # Используем фильтрацию через аннотации и агрегацию
        for genre_id in selected_genres:
            films = films.filter(genres__id=genre_id)

    # Фильтруем фильмы по названию, если есть поисковый запрос
    if search_query:
        films = films.filter(title__icontains=search_query)

    # Получаем все жанры для отображения на странице
    genres = Genre.objects.all()

    return render(request, 'main/film_filter.html', {
        'films': films,
        'genres': genres,
        'selected_genres': selected_genres,
        'search_query': search_query  # Передаём, чтобы отобразить в поле поиска
    })




def news(request):
    announc = News.objects.order_by('-date')
    return render(request, 'main/news.html',{'announ':announc})