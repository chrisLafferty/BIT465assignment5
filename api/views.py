from django.shortcuts import render
from rest_framework import viewsets
from .models import Breed, Dog
from .serializers import BreedSerializer, DogSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
