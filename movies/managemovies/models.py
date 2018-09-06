from django.db import models
	
class Movie (models.Model):
	title = models.CharField(max_length=200)
	actors = models.CharField(max_length=600)

	def __str__(self):
		return "Title: " + self.title + ", Actors: " + self.actors