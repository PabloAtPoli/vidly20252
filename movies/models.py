# Genre and Movie models
from django.db import models

class Genre(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Movie(models.Model):
	title = models.CharField(max_length=200)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')
	release_year = models.IntegerField()
	rental_unit_price = models.DecimalField(max_digits=6, decimal_places=2)
	units_in_inventory = models.PositiveIntegerField()
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Title: {self.title}, Genre: {self.genre.name}, Release Year: {self.release_year}, Rental Unit Price: {self.rental_unit_price}, Units in Inventory: {self.units_in_inventory}, Date Created: {self.date_created}"


# Create your models here.
