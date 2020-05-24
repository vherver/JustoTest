"""JustoExam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django_otp.admin import OTPAdminSite

from travels.views import AvgPassagerDay, AvgTravelRevenue, ReportStations
from buses.views import BestBus
from routes.views import ReportBusiestStations
from clients.views import ClientsView


# admin.site.__class__ = OTPAdminSite


urlpatterns = [
    path('admin/', admin.site.urls),
    path('avg/', AvgPassagerDay.as_view(), name='Avg travelers per day'),
    path('travel/', ReportStations.as_view(), name='Travel Reports'),
    path('travel/avg/', AvgTravelRevenue.as_view(), name='Avg revenue'),
    path('buses/', BestBus.as_view(), name='Avg revenue'),
    path('busiest_station/', ReportBusiestStations.as_view(), name='Avg revenue'),
    path('clients/', ClientsView.as_view(), name='Avg revenue'),

]
