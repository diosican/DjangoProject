from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def tz(request):
    return HttpResponse( timezone.now())
