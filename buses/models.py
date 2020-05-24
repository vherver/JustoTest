from django.db import models

import uuid


class Buses(models.Model):
    """
        Modelo que representa un Autobus, información basica.
    """

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False, unique=True)

    brand = models.CharField(verbose_name="Brand",
                            max_length=35,
                            unique=False,
                            blank=False)

    model = models.CharField(verbose_name="Model",
                             max_length=35,
                             unique=False,
                             blank=False)

    car_registration = models.CharField(verbose_name="Car Register",
                                        max_length=10,
                                        unique=True)

    creation_date = models.DateField(auto_now_add=True)

    active = models.BooleanField(default=True)

    clients_attended = models.BigIntegerField(default=0)

    class Meta:
        verbose_name = 'Bus'
        verbose_name_plural = 'Buses'

    def __str__(self):
        return self.car_registration
