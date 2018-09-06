from django.apps import AppConfig


class ManagemoviesConfig(AppConfig):
	name = 'managemovies'
	def ready(self):
		from .models import Movie
		Movie.objects.all().delete()
		f = open("movies.txt", "r")
		filecontent = f.read()
		films = filecontent.split("\n")
		if films[-1] == "":
			films.pop()
		i = 0
		while i < len(films):
			film = films[i].split(":")
			m = Movie(title=film[0], actors=film[1])
			m.save()
			i+=1