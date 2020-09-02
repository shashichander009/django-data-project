from django.shortcuts import render
from .models import Union, RegionData
# Create your views here.


def home_view(request):
    return render(request, "undata/home.html")


def problem1_view(request):

    countries = []

    print(RegionData.objects.all().count())

    years = RegionData.objects.filter(country='India').filter(year__lte=2006)

    countryqry = RegionData.objects.order_by(
        'country').values_list('country').distinct()

    countrieslist = list(countryqry)

    for country in countrieslist:
        countries.append(country[0])

    context = {
        "years": years,
        "range": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "countries": countries
    }

    return render(request, "undata/prob1.html", context)


def problem2_view(request):

    groups = []

    years = RegionData.objects.filter(country='India')

    grouplist = list(
        Union.objects.order_by('name').values_list('name').distinct())

    for group in grouplist:
        groups.append(group[0])

    context = {
        "years": years,
        "groups": groups
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

    grouplist = []

    years = RegionData.objects.filter(country='India').filter(year__lte=2010)

    groups = list(
        Union.objects.order_by('name').values_list('name').distinct())

    for group in groups:
        grouplist.append(group[0])

    context = {
        "years": years,
        "groups": grouplist
    }

    return render(request, "undata/prob4.html", context)
