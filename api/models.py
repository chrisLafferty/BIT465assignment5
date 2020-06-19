from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Breed(models.Model):
    name = models.CharField(max_length=32)
    size = models.CharField(max_length=32)
    friendliness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    sheddingAmount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

class Dog(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    favoriteFood = models.CharField(max_length=32)
    favoriteToy = models.CharField(max_length=32)


