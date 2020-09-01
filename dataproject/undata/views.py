from django.shortcuts import render, get_object_or_404, redirect
from .models import Union, RegionData
from django.http import JsonResponse
import json
import simplejson
# Create your views here.


def problem1_view(request):

    obj = RegionData.objects.filter(country='India').filter(year__lte=2006)

    countrieslist = list(
        RegionData.objects.order_by('country').values_list('country').distinct())
    finalList = []

    for country in countrieslist:
        finalList.append(country[0])

    context = {
        "object": obj,
        "range": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "countries": finalList
    }

    return render(request, "undata/index.html", context)


def problem1_response(request):

    if request.method == 'POST':
        print(request.POST)

    if request.method == 'GET':
        india_data = {}
        year = request.GET["year"]
        year_range = request.GET["range"]
        country = request.GET["country"]
        end_year = int(year)+int(year_range)-1
        print(end_year)

        qry = RegionData.objects.filter(
            country=country).filter(year__gte=year).filter(year__lte=end_year)

        for row in qry.all():
            yearkey = int(row.year)
            population_in_crores = round(row.population / 10000, 2)
            india_data[yearkey] = float(population_in_crores)

        return JsonResponse(india_data, safe=False)
