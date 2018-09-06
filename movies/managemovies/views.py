from django.http import HttpResponse

from .models import Movie

def index(request):
	f = open("movies.txt", "r")
	filecontent = f.read()
	films = filecontent.split("\n")

	return HttpResponse(films)