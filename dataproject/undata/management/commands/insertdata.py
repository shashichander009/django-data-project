from undata.models import Union
import csv
from django.core.management.base import BaseCommand
from undata.models import RegionData, Union


UNION_DICT = {
    "saarc": [
        4,
        50,
        64,
        356,
        462,
        524,
        586,
        144,
    ],
    "asean": [
        96,
        116,
        360,
        418,
        458,
        104,
        608,
        702,
        764,
        704,
    ],
    "brics": [
        76,
        643,
        356,
        156,
        710,
    ],
    "g4": [
        356,
        76,
        276,
        392,
    ],
    "g7": [
        124,
        250,
        276,
        380,
        392,
        826,
        840,
    ],
}


class Command(BaseCommand):

    def handle(self, *args, **options):

        for union_entry in UNION_DICT:
            country_ids = UNION_DICT[union_entry]
            for country in country_ids:
                union = Union()
                union.name = union_entry
                union.country_id = country
                union.save()

        print("Union Data Saved")

        with open('undata/rawdata/data.csv', 'r') as csv_file:

            csv_reader = csv.reader(csv_file)

            next(csv_reader)

            for line in csv_reader:
                regiondata = RegionData()
                regiondata.country = line[0]
                regiondata.code = line[1]
                regiondata.year = line[2]
                regiondata.population = line[3]
                regiondata.save()
            print("Region Data Saved")
