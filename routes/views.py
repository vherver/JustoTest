from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Count, Avg


from routes.models import Stations
from routes.serializers import StationSerializer
from travels.models import TravelClients


class ReportBusiestStations(generics.ListAPIView):
    serializer_class = StationSerializer

    def get_queryset(self):
        queryset = Stations.objects.all().order_by('people_in_station')
        return queryset
