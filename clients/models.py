from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

import uuid
from datetime import date



class Clients(models.Model):
    """
        Modelo que representa un Cliente, información basica y de contacto.
    """

    phone_regex = RegexValidator(
        regex='^\d{9,12}$',
        message=_('Phone number must be entered in the format: 5512345678. Up to 12 digits allowed.')
    )

    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
    )

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False, unique=True)

    name = models.CharField(verbose_name="Name",
                            max_length=35,
                            unique=False,
                            blank=False)

    last_name = models.CharField(verbose_name="Last Name",
                                 max_length=35,
                                 unique=False,
                                 blank=False)

    mother_name = models.CharField(verbose_name="Mothers Name",
                                   max_length=35,
                                   unique=False,
                                   blank=False,
                                   null=True)

    phone = models.CharField(max_length=12,
                             unique=True,
                             validators=[phone_regex, ])

    birthday = models.DateField(blank=True,
                                null=True)

    creation_date = models.DateField(auto_now_add=True)

    active = models.BooleanField(default=True)

    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              default='F')

    disability = models.BooleanField(default=False)

    travels_completed = models.BigIntegerField(default=0)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return str(self.id) + " " + self.name

    def client_age(self):
        today = date.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age

