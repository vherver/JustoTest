from rest_framework import serializers

from routes.models import Stations


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stations

        fields = '__all__'
