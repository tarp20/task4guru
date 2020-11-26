from django.urls import path, include
from .views import CarViewSet, RatingViewSet, CarsPopularViewSet

urlpatterns = [

    path('cars/', CarViewSet.as_view()),
    path('rate/', RatingViewSet.as_view()),
    path('popular/', CarsPopularViewSet.as_view()),

]
