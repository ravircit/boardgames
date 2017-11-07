from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Testing Git Commit")

def index(request):
    return HttpResponse("Testing Git Commit")
