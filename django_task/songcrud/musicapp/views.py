from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("ooo thanks you for been there for us we happy to see there !!")