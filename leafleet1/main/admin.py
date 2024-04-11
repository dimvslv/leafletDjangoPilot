from django.contrib import admin
from .models import CSVLocation

# вывод содержимого базы данных
# csv_locations = CSVLocation.objects.all()
# for location in csv_locations:
# print(location.object_name, location.longitude, location.latitude)

admin.site.register(CSVLocation)

print('helloworld!')
