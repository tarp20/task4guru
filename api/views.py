from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .models import Car, Rating
from .serializers import CarSerializers, RatingSerializer,\
    CarsPopularSerializer
from django.db.models import Avg, Count
from django.http import HttpResponse



def welcome(request):
    return HttpResponse("Hello! I'm working ")



class CarViewSet(ListCreateAPIView):
    serializer_class = CarSerializers

    def get_queryset(self):
        queryset = Car.objects.all()
        queryset = queryset.annotate(average_rank=Avg(
            'ratings__rating')).order_by('-average_rank')
        return queryset


class RatingViewSet(ListCreateAPIView):
    serializer_class = RatingSerializer

    def get_queryset(self):
        queryset = Rating.objects.all()

        return queryset


class CarsPopularViewSet(ListAPIView):
    serializer_class = CarsPopularSerializer

    def get_queryset(self):
        queryset = Car.objects.all()
        queryset = queryset.annotate(total_ratings=Count(
            'ratings')).order_by('-total_ratings')

        return queryset
