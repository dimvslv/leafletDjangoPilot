from django.shortcuts import render
from .models import CSVLocation

# Create your views here.


def index(request):
    bus_stops = list(CSVLocation.objects.values('longitude', 'latitude')[:100])
    # проверка содержимого словаря print(bus_stops[:10])
    context = {'bus_stops': bus_stops}
    return render(request, 'main/index.html', context)
