from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.views import generic

import redis
import json
import urllib2

r = redis.StrictRedis(host='localhost', port=1123, db=0)

def fill_db():
    r.set('movie:0', '{"Title": "Frozen", "Year": "2013", "Actors":"Kristen Bell, Idina Menzel, Jonathan Groff, Josh Gad" }')
    r.set('movie:1', '{"Title": "Avengers: Age of Ultron", "Year": "2015", "Actors":"Robert Downey Jr., Chris Hemsworth, Mark Ruffalo, Chris Evans" }')


fill_db()


def movies(request, movie_name):
	
	fill_db()

	movies_keys = r.keys('movie:*')
	movie_found = 'false'
	
	movie = {}

	for m in movies_keys:
		movie_m = json.loads(r.get(m))
		if movie_m['Title'] == movie_name:
			movie = movie_m
			movie_found = 'true'
	if movie_found == 'true':
		return render(request, 'movies/movie.html', {'movie': movie})
	else:
		return render(request,'movies/notfound.html',status=404)
	
