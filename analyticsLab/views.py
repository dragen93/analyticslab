from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def analyticsLab(request):
    return render(request, "analyticsLab/analyticsLab.html")