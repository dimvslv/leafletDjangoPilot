from django.db import models

# Create your models here.


class CSVLocation(models.Model):
    object_name = models.CharField(max_length=250)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.object_name
