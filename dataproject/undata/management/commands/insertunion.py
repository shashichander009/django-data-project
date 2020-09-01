import csv
from django.core.management.base import BaseCommand
from undata.models import Union


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
    ]
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
