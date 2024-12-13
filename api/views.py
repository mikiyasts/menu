from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from restaurant .models import Restaurant,MenuItem,Category
from .serializers import RestorantSerializer
import logging
logger=logging.getLogger(__name__)
#api endpoints
@api_view(['GET'])
def api_endpoints(request):
    endpoints = {
        "": "",
    }
    return Response(endpoints)

#restorants
@api_view(['GET'])
def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    serializer = RestorantSerializer(restaurants, many=True)
    return Response(serializer.data,status=200)

@api_view(['GET'])
def restaurant_deatil_list(request, pk):
    try:
     restaurants=Restaurant.objects.get(id=pk)
     if restaurants:
         serializer=RestorantSerializer(restaurants)
         return Response(serializer.data,status=200)
     else:
         return Response({'restaurant with this id does not exist'},status=400)
         
    except:
        return Response({'something went wrong'},status=500)
        
        
    
     
 