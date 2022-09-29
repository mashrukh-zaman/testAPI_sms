from urllib import response
from django.shortcuts import render

from . import sms
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def send_sms(request):
    if request.method == 'GET':
        return HttpResponse('hell', 'safe=False')
    # elif request.method == 'POST':

