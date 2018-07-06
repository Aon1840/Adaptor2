from django.db import models
from Zones.models import Zone

class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    position_name = models.CharField(max_length=10,blank=False)
    is_avaliable = models.BooleanField(default=True,blank=False)
    zone_id = models.ForeignKey(Zone, on_delete=models.CASCADE)

    class Meta:
        ordering = ('position_id',)