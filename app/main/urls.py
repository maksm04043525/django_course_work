from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('actors/', views.actor_list, name = 'actor_list'),
    path('actor/<int:actor_id>/', views.actor_detail, name = 'actor_detail'),
    path('film/<int:film_id>/', views.film_detail, name = 'film_detail'),
    path('films/filter', views.film_filter, name='film_filter'),
    path('news/', views.news, name='news'),
]
