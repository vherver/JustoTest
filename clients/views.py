from rest_framework import generics

from clients.models import Clients
from clients.serializers import ClientSerializer

from datetime import datetime


class ClientsView(generics.ListAPIView):
    serializer_class = ClientSerializer

    def get_queryset(self):

        date = datetime.today()

        queryset = Clients.objects.filter(gender=self.request.query_params['gender'],
                                          disability=self.request.query_params['disability'],
                                          travels_completed__exact=self.request.query_params['travels'],
                                          birthday__day=date.day,
                                          birthday__month=date.month,
                                          birthday__year=date.year - int(self.request.query_params['age'])
                                          )
        return queryset
