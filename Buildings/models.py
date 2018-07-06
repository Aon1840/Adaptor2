from django.db import models

class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    building_name = models.CharField(max_length=30,blank=False)

    class Meta:
        ordering = ('building_id',)