import challenges
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

monthly_challenges = {
    'january': 'January Tasks Todo',
    'february': 'february Tasks <br> Todo',
    'march': 'march Tasks <br> Todo',
    'april': 'april Tasks <br> Todo',
    'may': 'May Tasks <br> Todo',
    'june': 'june Tasks <br> Todo',
    'july': 'july Tasks <br> Todo',
    'august': 'august Tasks <br> Todo',
    'september': 'september Tasks <br> Todo',
    'october': 'october Tasks <br> Todo',
    'november': 'november Tasks <br> Todo',
    'december': 'december Tasks <br> Todo',
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month]
    return HttpResponseRedirect(redirect_month)


def monthly_challenge(request, month):
    try:
        challenges_text = monthly_challenges[month]
        return HttpResponse(challenges_text)
    except:
        return HttpResponseNotFound("This is not the month")
