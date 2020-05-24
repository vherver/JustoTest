from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Count, Avg


from travels.models import TravelClients, Travel
from travels.serializers import TravelSerializer

from datetime import datetime, timedelta


class AvgPassagerDay(generics.GenericAPIView):
    def get(self, request):

        clients = TravelClients.objects.values('travel').filter(travel__travel_status='FINISHED')

        travels = Travel.objects.values('arrival_date__date').filter(travel_status='FINISHED').order_by('arrival_date')

        elaspsed = travels.last()['arrival_date__date'] - travels.first()['arrival_date__date']

        return Response(status=status.HTTP_200_OK, data={"avg": len(clients) / elaspsed.days})


class AvgTravelRevenue(generics.GenericAPIView):
    def get(self, request):

        travels = Travel.objects.filter(travel_status='FINISHED')

        travels_revenue = travels.aggregate(revenue_avg=Avg('revenue'))
        travels_time = travels.aggregate(time_avg=Avg('time_to_complete'))

        elapsed_time_avg = timedelta(seconds=int(travels_time['time_avg']))

        return Response(status=status.HTTP_200_OK, data={"avg_revenue": travels_revenue['revenue_avg'],
                                                         "avg_time": str(elapsed_time_avg)})


class ReportStations(generics.ListAPIView):
    serializer_class = TravelSerializer

    def get_queryset(self):
        queryset = Travel.objects.filter(travel_status='FINISHED',
                                         route__origin__id=self.request.query_params['origin'],
                                         route__destination__id=self.request.query_params['destination'])
        return queryset


