from django.shortcuts import render, get_object_or_404, redirect
from .models import Union, RegionData
from django.http import JsonResponse
import json
import simplejson
# Create your views here.


def home_view(request):

    obj = RegionData.objects.filter(country='India')

    countries = RegionData.objects.order_by().values_list('country').distinct()

    context = {
        "object": obj,
        "range": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "countries": countries
    }

    return render(request, "undata/index.html", context)


def problem1_view(request):

    if request.method == 'POST':
        print(request.POST)

    if request.method == 'GET':
        india_data = {}
        year = request.GET["year"]
        year_range = request.GET["range"]

        print(year)
        print(year_range)

        end_year = int(year)+int(year_range)-1

        print(end_year)

        qry = RegionData.objects.filter(
            country='India').filter(year__gte=year).filter(year__lte=end_year)

        for row in qry.all():
            yearkey = int(row.year)
            population_in_crores = round(row.population / 10000, 2)
            india_data[yearkey] = float(population_in_crores)

        return JsonResponse(india_data, safe=False)
