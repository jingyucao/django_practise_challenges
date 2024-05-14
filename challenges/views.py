from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

# This is dummy data
# def january(request):
#     return HttpResponse("Hello, world. This is for January.")

monthly_challenges = {
    'january': "January - Eat no meat for the entire month!",
    'february': "February - Walk for at least 20 minutes every day!",
    'march': "March - Learn Django for at least 20 minutes every day!",
    'april': "April - Eat meat for the entire month!",
    'may': "May - Boulder a lot!",
    'june': "June - Learn Django more!",
    'july': "July - Eat eggs for the entire month!",
    'august': "August - Beat 81 sometimes!",
    'september': "September - Learn a lot of Django!",
    'october': "October - Eat vegetables for the entire month!",
    'november': "November - Walk walk walk!",
    'december': "December - Learn something else!"
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month!')
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect('/challenges/' + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This month is not supported!')
