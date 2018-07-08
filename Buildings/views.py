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
        return JsonResponse(serializer.data,safe=False)

#     -----------------------------  TEST Method  -------------------------------------------
@csrf_exempt
def testAddBuilding(request):
    serialzer = BuildingSerializer(data=request.POST)
    if serialzer.is_valid():
        serialzer.save()
        return JsonResponse(serialzer.data, status=201)

    return JsonResponse(serialzer.errors, status=400)

@csrf_exempt
def testEditBuilding(request, building_id):

    try:
        building = Building.objects.get(building_id=building_id)
    except Building.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BuildingSerializer(building, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)

        return JsonResponse(serializer.errors, status=400)

    # data = JSONParser().parse(request)
    # serializer = SnippetSerializer(snippet, data=data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return JsonResponse(serializer.data)
    # return JsonResponse(serializer.errors, status=400)

