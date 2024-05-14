from django.urls import path
from . import views

# This is dummy data
# urlpatterns = [
#     path('january', views.january),
#     path('february', views.february),
# ]

# with the <>, we don't need to create a new path for each month
urlpatterns = [
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge)
]
