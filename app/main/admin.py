from django.contrib import admin

from .models import Actor, Film, Genre, News, Comment

admin.site.register(Actor)
admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(News)
admin.site.register(Comment)