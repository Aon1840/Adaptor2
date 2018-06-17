from django.db import models

# Create your models here.
# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=15,blank=False)
#     password = models.CharField(max_length=20,blank=False)
#     name = models.CharField(max_length=30,blank=False)
#     surname = models.CharField(max_length=30,blank=False)
#     tel = models.CharField(max_length=10,blank=False)
#     email = models.EmailField(max_length=50,blank=False)
#     register_date = models.DateTimeField(auto_now_add=True,blank=False)
#
#     class Meta:
#         ordering = ('user_id',)

# Building Database
class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    building_name = models.CharField(max_length=30,blank=False)

    class Meta:
        ordering = ('building_id',)


# Floor Database
class Floor(models.Model):
    floor_id = models.AutoField(primary_key=True)
    floor_name = models.CharField(max_length=10,blank=False)
    avaliable_parking = models.IntegerField(blank=False)
    total_parking = models.IntegerField(blank=False)
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)

    class Meta:
        ordering = ('floor_id',)


# Zone Database
class Zone(models.Model):
    zone_id = models.AutoField(primary_key=True)
    zone_name = models.CharField(max_length=10,blank=False)
    avaliable_parking = models.IntegerField(blank=False)
    total_parking = models.IntegerField(blank=False)
    floor_id = models.ForeignKey(Floor, on_delete=models.CASCADE)

    class Meta:
        ordering = ('zone_id',)


# Position Database
class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    position_name = models.CharField(max_length=10,blank=False)
    is_avaliable = models.BooleanField(default=True,blank=False)
    zone_id = models.ForeignKey(Zone, on_delete=models.CASCADE)

    class Meta:
        ordering = ('position_id',)


