from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        list_items += f"<li><a href='{month}'>{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('<h1>Invalid month!</h1>')

    redirect_month = months[month - 1]

    # reverse create a path looks like '/challenge', then add args as an array to have the exact path '/challenge/may'
    redirect_path = reverse('monthly-challenge', args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f'<h1>{challenge_text}</h1>'
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h1>This month is not supported!</h1>')
