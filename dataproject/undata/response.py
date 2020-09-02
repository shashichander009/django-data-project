from django.http import JsonResponse
from django.db.models import Sum
from .models import Union, RegionData


def problem1_response(request):

    if request.method == 'GET':

        year = request.GET["year"]
        year_range = request.GET["range"]
        country = request.GET["country"]
        end_year = int(year)+int(year_range)-1

        qry = RegionData.objects.filter(
            country=country).filter(year__gte=year).filter(year__lte=end_year)

        response_data = {}

        for row in qry.all():
            yearkey = int(row.year)
            population_in_crores = round(row.population / 10000, 2)
            response_data[yearkey] = float(population_in_crores)

        return JsonResponse(response_data)
    else:
        print("Invalid Request Method")


def problem2_response(request):

    if request.method == 'GET':

        response_data = {}

        year = request.GET["year"]
        group = request.GET["group"]

        qry = Union.objects.filter(name=group)

        unionlist = []

        for group in qry.all():
            unionlist.append(group.country_id)

        qry = RegionData.objects.filter(code__in=unionlist).filter(year=year)

        for row in qry.all():
            population_in_crores = round(row.population / 10000, 2)
            response_data[row.country] = float(population_in_crores)

        return JsonResponse(response_data)
    else:
        print("Invalid Request Method")


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

        response_data = {}

        for row in qry.all():
            population_in_crores = round(row['sum'] / 10000, 2)
            response_data[row['year']] = float(population_in_crores)

        return JsonResponse(response_data)

    else:
        print("Invalid Request Method")


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

        response_data = {}

        for row in qry.all():
            country = str(row.country)
            current_year = str(row.year)
            population_in_crores = round(float(row.population) / 10000, 2)

            if response_data.get(country) is None:
                response_data[country] = {
                    current_year: population_in_crores}
            else:
                nation_object = response_data[country]
                nation_object[current_year] = population_in_crores

        return JsonResponse(response_data)

    else:
        print("Invalid Request Method")
