from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Buildings.models import Building
from Emulators.serializers import BuildingSerializer
import json

# Create your views here.
@csrf_exempt
def getAllBuilding(request):
    if request.method == 'GET':
        buildings = Building.objects.all()
        serializer = BuildingSerializer(buildings, many=True)
        return JsonResponse(serializer, safe=False)

#     -----------------------------  TEST Method  -------------------------------------------
@csrf_exempt
def testAddBuilding(request):
    serialzer = BuildingSerializer(data=request.POST)
    if serialzer.is_valid():
        serialzer.save()
        return JsonResponse(serialzer.data, status=201)

    return JsonResponse(serialzer.errors, status=400)

# @csrf_exempt
# def testEditBuilding(request):