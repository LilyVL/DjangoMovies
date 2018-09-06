from django.http import HttpResponse
from django.template import loader
from .models import Movie
from django.shortcuts import get_object_or_404, render


def index(request):
	films = Movie.objects.all()
	titles = []
	i=0
	while i < len(films):
		title = films[i].title
		titles.append(title)
		i+=1
	template = loader.get_template('managemovies/index.html')
	context = {
		'movies': films,
	}
	return HttpResponse(template.render(context, request))	

def details(request, movie_id):
	movie = Movie.objects.get(pk=movie_id)
	template = loader.get_template('managemovies/details.html')
	context = {
		'movie': movie,
	}
	return HttpResponse(template.render(context, request))	