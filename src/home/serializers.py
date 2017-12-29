from rest_framework import routers, serializers, viewsets , permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



from .models import Weather, WeatherCreate

class WeatherSerializer(serializers.ModelSerializer):
    # time = serializers.DateField(format="%Y-%m-%d %H:%M:%S")
    time = serializers.SerializerMethodField(read_only = True)
    def get_time(self,instance):
        date = instance.time.date().strftime('%d/%m/%Y')
        return date
    class Meta:
        model = Weather
        fields = [
            'id',
            'day_name',
            'temperature',
            'weather',
            'time',
        ]

class WeatherCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherCreate
        fields = [
            'id',
            'day_name',
            'temperature',
            'weather',
            'time',
        ]
