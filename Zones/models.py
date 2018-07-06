from django.db import models
from Floors.models import Floor

class Zone(models.Model):
    zone_id = models.AutoField(primary_key=True)
    zone_name = models.CharField(max_length=10,blank=False)
    avaliable_parking = models.IntegerField(blank=False)
    total_parking = models.IntegerField(blank=False)
    floor_id = models.ForeignKey(Floor, on_delete=models.CASCADE)

    class Meta:
        ordering = ('zone_id',)