from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapiis.serializer import TodoSerializer
from myapiis.models import apii

# Create your views here.

@api_view(['GET'])
def fetchall(request):
    alltodo = apii.objects.all().order_by("-id")
    mydata = TodoSerializer(alltodo, many = True)

    return Response({
        "message" : "Data Fetch Sucessfully",
        "data" : mydata.data
    })
@api_view(['POST'])
def savedata(request):
    serlizedata = TodoSerializer(data = request.data)
    if serlizedata.is_valid():
        serlizedata.save()

    return Response({
        "message" : "Data saved Sucessfully",
        "data" : serlizedata.data
    })
@api_view(['GET'])

def singledata(request, id):
    alltodo = apii.objects.get(id = id)
    mydata = TodoSerializer(alltodo)

    return Response({
        "message" : "todo feethc Sucessfully",
        "data" : mydata.data
    })
