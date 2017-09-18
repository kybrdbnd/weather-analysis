from django.conf.urls import url
from .views import (home, weather, station, save_stations)

urlpatterns = [
    url(r'^$', weather, name='weather'),
    url(r'^station/', station, name='station'),
    url(r'^save_station/', save_stations, name='save_station'),
]
