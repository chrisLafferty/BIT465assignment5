from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Breed, Dog
from .serializers import BreedSerializer, DogSerializer


class BreedList(APIView):

    def get(self, request, format=None):
        breed = Breed.objects.all()
        serializer = BreedSerializer(breed, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BreedDetail(APIView):

    def get_object(self, pk):
        try:
            return Breed.object.get(pk=pk)
        except Breed.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        breed = self.get_object(pk)
        serializer = BreedSerializer(breed)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        breed = self.get_object(pk)
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DogList(APIView):

    def get(self, request, format=None):
            dog = Dog.objects.all()
            serializer = DogSerializer(dog, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogDetail(APIView):

    def get_object(self, pk):
        try:
            return Dog.object.get(pk=pk)
        except Dog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dog = self.get_object(pk)
        serializer = DogSerializer(dog)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dog = self.get_object(pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#class BreedViewSet(viewsets.ModelViewSet):
   # queryset = Breed.objects.all()
   # serializer_class = BreedSerializer


#class DogViewSet(viewsets.ModelViewSet):
    #queryset = Dog.objects.all()
    #serializer_class = DogSerializer
