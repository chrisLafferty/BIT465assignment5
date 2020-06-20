
from django.urls import path
#from rest_framework import routers
#from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
#from .views import BreedViewSet, DogViewSet
from api import views

#router = routers.DefaultRouter()
#router.register('breed', BreedViewSet)
#router.register('dog', DogViewSet)

urlpatterns = [
    path('api/', views.BreedList.as_view()),
    path('api/<int:pk>', views.BreedDetail.as_view()),
    path('api/', views.DogList.as_view()),
    path('api/<int:pk>', views.DogDetail.as_view()),
    #path('', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)

