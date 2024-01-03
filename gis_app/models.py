from django.db import models
from django.contrib.gis.db import models as gismodels

class Location(gismodels.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    geometry = gismodels.GeometryField(blank=True, null=True , db_index=True)

    def __str__(self):
        return self.name


