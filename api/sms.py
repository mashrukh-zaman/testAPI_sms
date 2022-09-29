from urllib import response
from django.shortcuts import render
import requests
import json

# Create your views here.
url = "https://sms.shurjobarta.com.bd/api/v1/sms"

headers = {"token" : "Bearer 5Z6k4Q6-UGFanwV-E6BahoZ6iwK0jL-61664345434491"}

data = {
    "receiver" : "01751422552",
    "maskname" : "",
    "message"  : "Test message",
    "priority" : "HIGH",
    "routeType" : "LOCAL"
}


