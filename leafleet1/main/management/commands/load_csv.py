import csv
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from ...models import CSVLocation


class Command(BaseCommand):
    help = 'Load data from csv file'

    def handle(self, *args, **kwargs):
        file = os.path.join(settings.BASE_DIR, 'csv', 'gis_osm_transport_free_1_almaty.csv')
        keys = ('fclass', 'xcoord', 'ycoord')

        records = []
        with open(file, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                records.append({k: row[k] for k in keys})

            for record in records:
                CSVLocation.objects.get_or_create(
                    object_name=record['fclass'],
                    longitude=record['xcoord'],
                    latitude=record['ycoord'],
                )
