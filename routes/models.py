from django.db import models

import uuid


class Stations(models.Model):
    """
           Modelo que representa Estaciones de autobuses.
    """

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False, unique=True)

    station_name = models.CharField(verbose_name="Station name",
                                    max_length=35,
                                    unique=True,
                                    blank=False)

    creation_date = models.DateField(auto_now_add=True)

    people_in_station = models.BigIntegerField(default=0)

    class Meta:
        verbose_name = 'Station'
        verbose_name_plural = 'Stations'


    def __str__(self):
        return self.station_name


class Costs(models.Model):
    """
           Modelo que representa grupo de costos para viajes.
    """

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False, unique=True)

    child = models.DecimalField(verbose_name="Children costs",
                                max_digits=10,
                                decimal_places=2)

    adult = models.DecimalField(verbose_name="Adult costs",
                                max_digits=10,
                                decimal_places=2)

    third_age = models.DecimalField(verbose_name="Third age costs",
                                    max_digits=10,
                                    decimal_places=2)

    class Meta:
        verbose_name = 'Cost'
        verbose_name_plural = 'Cost'


class Routes(models.Model):
    """
        Modelo que representa un Rutas, indicando origen y destino.
    """

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False, unique=True)

    origin = models.ForeignKey("routes.Stations",
                               on_delete=models.PROTECT,
                               related_name="Origin_Station")

    destination = models.ForeignKey("routes.Stations",
                                    on_delete=models.PROTECT,
                                    related_name="Destination_Station")

    cost = models.ForeignKey("routes.Costs",
                             on_delete=models.PROTECT)

    travel_expense = models.DecimalField(verbose_name="Travel costs",
                                         max_digits=10,
                                         decimal_places=2)

    creation_date = models.DateField(auto_now_add=True)

    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'

    def __str__(self):
        return str(self.origin) + "-" + str(self.destination)

