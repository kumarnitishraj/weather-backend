
from django.db.models import Count

#from django.views import View

# Create your views here.


from rest_framework import status
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.parsers import FormParser,MultiPartParser,JSONParser


# Test Import

import json
from .serializers import (WeatherSerializer,WeatherCreateSerializer)
from .models import Weather

from .utils import (
                    notacceptable,
                    unauthorized,
                    failure_400,
					forbidden_403,
                    success
                    )



"""
	This class give us user  Profile detail
"""
class WeatherDetailAPIView(APIView):
    def get(self, request, format=None):
        try:
            queryset = Weather.objects.all()
            serializer = WeatherSerializer(queryset,context={'request': request}, many = True)
            # response,responseStatus = success(serializer.data,status.HTTP_200_OK)
            return Response(serializer.data,status = status.HTTP_200_OK)

        except Exception as e:
            print(e)
            response, responseStatus = failure_400()
            return Response(response, responseStatus)


    def post(self, request, format=None):
        try:
            data = request.data
            serializer = WeatherCreateSerializer(data = data,context={'request': request})
            if serializer.is_valid():
                serializer.save()
                response,responseStatus = success(serializer.data,status.HTTP_200_OK)
                return Response(response,responseStatus)

        except Exception as e:
            print(e)
            response, responseStatus = failure_400()
            return Response(response, responseStatus)
