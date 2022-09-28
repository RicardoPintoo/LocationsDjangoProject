from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=200)
    population = models.PositiveBigIntegerField()

    def __str__(self):
        return f'{self.name} with {self.population} people'

class Person(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Location(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    persons = models.ManyToManyField(Person, blank=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.slug}'