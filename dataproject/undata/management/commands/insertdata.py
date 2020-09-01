import csv
from django.core.management.base import BaseCommand
from undata.models import RegionData


class Command(BaseCommand):

    def handle(self, *args, **options):

        with open('data.csv', 'r') as csv_file:

            csv_reader = csv.reader(csv_file)

            next(csv_reader)

            for line in csv_reader:
                regiondata = RegionData()
                regiondata.country = line[0]
                regiondata.code = line[1]
                regiondata.year = line[2]
                regiondata.population = line[3]
                regiondata.save()
