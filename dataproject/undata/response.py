
from django.shortcuts import render, get_object_or_404, redirect
from .models import Union, RegionData
from django.http import JsonResponse
import json
import simplejson
from django.db.models import Sum


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


def problem2_response(request):

    if request.method == 'GET':
        group_data = {}
        year = request.GET["year"]
        group = request.GET["group"]

        print("solving problem 2")

        qry = Union.objects.filter(name=group)

        finalList = []

        for group in qry.all():
            finalList.append(group.country_id)

        print(finalList)

        qry = RegionData.objects.filter(code__in=finalList).filter(year=year)

        for row in qry.all():
            population_in_crores = round(row.population / 10000, 2)
            group_data[row.country] = float(population_in_crores)

        return JsonResponse(group_data, safe=False)


def problem3_response(request):

    if request.method == 'GET':

        year = request.GET["year"]
        group = request.GET["group"]
        year_range = request.GET["range"]
        end_year = int(year)+int(year_range)-1

        groupquery = Union.objects.filter(name=group)

        groupcountrylist = []

        for group in groupquery.all():
            groupcountrylist.append(group.country_id)

        qry = RegionData.objects.filter(code__in=groupcountrylist)

        qry = qry.filter(year__gte=year).filter(year__lte=end_year)

        qry = qry.values('year').order_by(
            'year').annotate(sum=Sum('population'))

        group_data = {}

        for row in qry.all():
            population_in_crores = round(row['sum'] / 10000, 2)
            group_data[row['year']] = float(population_in_crores)

        return JsonResponse(group_data, safe=False)


def problem4_response(request):

    if request.method == 'GET':

        year = request.GET["year"]
        group = request.GET["group"]
        end_year = int(year)+4

        groupquery = Union.objects.filter(name=group)

        groupcountrylist = []

        for group in groupquery.all():
            groupcountrylist.append(group.country_id)

        qry = RegionData.objects.filter(code__in=groupcountrylist)

        qry = qry.filter(year__gte=year).filter(year__lte=end_year)

        asean_grp_data = {}

        for row in qry.all():
            country = str(row.country)
            current_year = str(row.year)
            population_in_crores = round(float(row.population) / 10000, 2)

            if asean_grp_data.get(country) is None:
                asean_grp_data[country] = {
                    current_year: population_in_crores}
            else:
                nation_object = asean_grp_data[country]
                nation_object[current_year] = population_in_crores

        return JsonResponse(asean_grp_data, safe=False)
