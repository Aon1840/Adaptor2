# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Users.models import User
from Users.serializers import UserSerializer
import json

# Create your views here.

# @csrf_exempt
# def getAllUser(request):
#     #method for list all users
#
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return JsonResponse(serializer.data,safe=False)
#
#
# @csrf_exempt
# def getUserDetail(request,pk):
#     #method for see user detail
#
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = UserSerializer(user, many=False)
#
#         return JsonResponse(serializer.data)
#
#
# @csrf_exempt
# def AddNewUser(request):
#         #method for add new user
#
#         serializer = UserSerializer(data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
#
#
#
#
