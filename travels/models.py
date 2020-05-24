from django.db import models
from django.db.models import Sum


import uuid
from buses.models import Buses
from clients.models import Clients


class Travel(models.Model):
    """
           Modelo que representa Estaciones de autobuses.
    """

    TRAVEL_STATUS_CHOICES = (
        ('PLANED', 'Travel Planed'),
        ('STARTED', 'Bus on origin station'),
        ('FINISHED', 'Travel completed'),
    )

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False, unique=True)

    route = models.ForeignKey("routes.Routes",
                              on_delete=models.PROTECT)

    bus = models.ForeignKey("buses.Buses",
                            on_delete=models.PROTECT)

    travel_status = models.CharField(max_length=10,
                                     choices=TRAVEL_STATUS_CHOICES,
                                     default='PLANED')

    creation_date = models.DateField(auto_now_add=True)

    planed_start_date = models.DateTimeField(default=None,
                                             blank=True,
                                             null=True)


    departure_date = models.DateTimeField(default=None,
                                             blank=True,
                                             null=True)

    arrival_date = models.DateTimeField(default=None,
                                        blank=True,
                                        null=True)

    time_to_complete = models.BigIntegerField(default=0)

    creation_date = models.DateField(auto_now_add=True)

    revenue = models.DecimalField(verbose_name="Travel revenue",
                                  max_digits=10,
                                  decimal_places=2,
                                  default=0.0,
                                  editable=False)


    class Meta:
        verbose_name = 'Travel'
        verbose_name_plural = 'Travels'

    def __str__(self):
        return str(self.route) + "-" + self.planed_start_date.strftime("%m/%d/%Y, %H:%M:%S")

    def save(self, *args, **kwargs):

        if self.arrival_date:
            self.travel_status = 'FINISHED'

            if self.revenue == 0.0:
                clients_in_travel = TravelClients.objects.filter(travel=self.id)

                revenue_partial = clients_in_travel.aggregate(Sum('ticket_cost'))['ticket_cost__sum'] \
                    if len(clients_in_travel) > 0 else 0.0
                self.revenue = revenue_partial \
                               - self.route.travel_expense

                self.time_to_complete = (self.arrival_date - self.departure_date).seconds

                self.bus.clients_attended += len(clients_in_travel)

                self.bus.revenue += self.revenue

                self.bus.save()

                self.route.origin.people_in_station += len(clients_in_travel)
                self.route.origin.save()
                self.route.destination.people_in_station += len(clients_in_travel)
                self.route.destination.save()

                for client_in_travel in clients_in_travel:
                    client_in_travel.client.travels_completed += 1
                    client_in_travel.client.save()



        super(Travel, self).save(*args, **kwargs)


class TravelClients(models.Model):
    """
           Modelo que relaciona que usuarios viajaron en un viaje.
    """

    travel = models.ForeignKey("travels.Travel",
                               on_delete=models.PROTECT)

    client = models.ForeignKey("clients.Clients",
                               on_delete=models.PROTECT)

    ticket_cost = models.DecimalField(verbose_name="Ticket Cost",
                                      max_digits=10,
                                      decimal_places=2,
                                      default=0.0,
                                      editable=False)

    class Meta:
        verbose_name = 'Travel Client'
        verbose_name_plural = 'Travel Clients'

    def save(self, *args, **kwargs):

        if self.ticket_cost == 0.0:
            costs = self.travel.route.cost

            client_age = self.client.client_age()

            if client_age < 18:
                self.ticket_cost = costs.child

            elif client_age > 65:
                self.ticket_cost = costs.third_age

            else:
                self.ticket_cost = costs.adult

        super(TravelClients, self).save(*args, **kwargs)


