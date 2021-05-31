import challenges
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def monthly_challenge(request, month):
    challenges_text = None
    if month == 'january':
        challenges_text = "January Challenges List Here"
    elif month == 'febrauary':
        challenges_text = "Febrauary Challenges List Here"
    elif month == 'march':
        challenges_text = "March Challenges List Here"
    else:
        return HttpResponseNotFound("IS This the name of the month ?")
    return HttpResponse(challenges_text)
def monthly_challenge_by_number(request, month):
    return HttpResponse(month)