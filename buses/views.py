from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Count, Avg


from buses.models import Buses
from buses.serializers import BusesSerializer


class BestBus(generics.ListAPIView):
    queryset = Buses.objects.all().order_by('-clients_attended')[:1]
    serializer_class = BusesSerializer


class BusRevenue(generics.ListAPIView):
    queryset = Buses.objects.all().order_by('-revenue')[:1]
    serializer_class = BusesSerializer