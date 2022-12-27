from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello There. I am testing django testing through AWS codebuild")
# Create your views here.
