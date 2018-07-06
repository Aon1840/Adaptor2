from django.db import models
from Buildings.models import Building

class Floor(models.Model):
    floor_id = models.AutoField(primary_key=True)
    floor_name = models.CharField(max_length=10,blank=False)
    avaliable_parking = models.IntegerField(blank=False)
    total_parking = models.IntegerField(blank=False)
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)

    class Meta:
        ordering = ('floor_id',)