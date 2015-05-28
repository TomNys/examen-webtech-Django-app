from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'movies/(?P<movie_name>[A-z .0-9 .:]+)/$', views.movies, name='movie'),
]