from django.shortcuts import render, get_object_or_404, redirect
from .models import Union, RegionData
from django.http import JsonResponse
import json
import simplejson
from django.db.models import Sum
# Create your views here.


def home_view(request):
    return render(request, "undata/home.html")


def problem1_view(request):

    years = RegionData.objects.filter(country='India').filter(year__lte=2006)

    countrieslist = list(
        RegionData.objects.order_by('country').values_list('country').distinct())
    finalList = []

    for country in countrieslist:
        finalList.append(country[0])

    context = {
        "years": years,
        "range": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "countries": finalList
    }

    return render(request, "undata/prob1.html", context)


def problem2_view(request):

    years = RegionData.objects.filter(country='India')

    countrieslist = list(
        Union.objects.order_by('name').values_list('name').distinct())
    finalList = []

    for country in countrieslist:
        finalList.append(country[0])

    context = {
        "years": years,
        "countries": finalList
    }

    return render(request, "undata/prob2.html", context)


def problem3_view(request):

    years = RegionData.objects.filter(country='India').filter(year__lte=2006)

    groups = list(
        Union.objects.order_by('name').values_list('name').distinct())
    finalList = []

    for group in groups:
        finalList.append(group[0])

    context = {
        "years": years,
        "range": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "groups": finalList
    }

    return render(request, "undata/prob3.html", context)


def problem4_view(request):

    years = RegionData.objects.filter(country='India').filter(year__lte=2010)

    groups = list(
        Union.objects.order_by('name').values_list('name').distinct())
    finalList = []

    for group in groups:
        finalList.append(group[0])

    context = {
        "years": years,
        "groups": finalList
    }

    return render(request, "undata/prob4.html", context)
