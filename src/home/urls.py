from django.conf.urls import url
from django.contrib import admin

from . views import(
    WeatherDetailAPIView
)


urlpatterns = [
        url(r'^$', WeatherDetailAPIView.as_view() , name='weather_api'),
]
