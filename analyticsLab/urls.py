from django.urls import path
from . import views

urlpatterns = [
    path('analyticsLab',views.analyticsLab, name="analyticslab"),
    path('searchDatabase',views.searchDatabase, name="searchDatabase"),
]

