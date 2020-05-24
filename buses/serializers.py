from rest_framework import serializers

from buses.models import Buses


class BusesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buses

        fields = '__all__'
