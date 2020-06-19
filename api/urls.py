
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import BreedViewSet, DogViewSet

router = routers.DefaultRouter()
router.register('breed', BreedViewSet)
router.register('dog', DogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

