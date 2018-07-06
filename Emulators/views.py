from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from CarPositions.models import CarPosition
from Users.models import User
from CarPositions.serializers import CarPositionSerializer
import firebase_admin
from firebase_admin import credentials
import json

# Create your views here.
