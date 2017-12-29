
from django.db import models
import Weather.settings as settings

class Weather(models.Model):

    day_name = models.CharField(max_length=200,null=True,blank=True)
    temperature = models.CharField(blank=True,null=True,max_length=5,default=0)

    weather = models.CharField(max_length=30,null = True,blank = True,)


    time = models.DateTimeField( editable=True)




    def __str__(self):
        return str(self.day_name)

class WeatherCreate(models.Model):

    day_name = models.CharField(max_length=200,null=True,blank=True)
    temperature = models.CharField(blank=True,null=True,max_length=5,default=0)

    weather = models.CharField(max_length=30,null = True,blank = True,)


    time = models.DateTimeField( editable=True,auto_now=True)




    def __str__(self):
        return str(self.day_name)
