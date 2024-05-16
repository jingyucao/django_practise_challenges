from django.urls import path
from . import views

# with the <>, we don't need to create a new path for each month
urlpatterns = [
    path("", views.index, name='index'),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name='monthly-challenge')
]
