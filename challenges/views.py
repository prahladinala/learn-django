from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("This Works!")

def february(request):
    return HttpResponse("Walk for atleast 20 min every day")