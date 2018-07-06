from rest_framework import serializers
from Buildings.models import Building
from Floors.models import Floor
from Zones.models import Zone
from Positions.models import Position

# //////////////////////////////////////////////// BUILDINGS ////////////////////////////////////////////////
class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ('building_id','building_name')

    def create(self, validated_data):
        return Building.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.building_name = validated_data.get('building_name',instance)
        instance.save()

        return instance
# //////////////////////////////////////////////// BUILDINGS ////////////////////////////////////////////////


# //////////////////////////////////////////////// FLOORS ////////////////////////////////////////////////
class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = ('floor_id','floor_name','avaliable_parking','total_parking','building_id')

    def create(self, validated_data):
        return Floor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.floor_name = validated_data.get('floor_name',instance.floor_name)
        instance.avaliable_parking = validated_data.get('avaliable_parking',instance.avaliable_parking)
        instance.total_parking = validated_data.get('total_parking',instance.total_parking)
        instance.save()

        return instance
# //////////////////////////////////////////////// FLOORS ////////////////////////////////////////////////


# //////////////////////////////////////////////// ZONES ////////////////////////////////////////////////
class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ('zone_id','zone_name','avaliable_parking','total_parking','floor_id')

    def create(self, validated_data):
        return Zone.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.zone_name = validated_data.get('zone_name',instance.zone_name)
        instance.avaliable_parking = validated_data.get('avaliable_parking',instance.avaliable_parking)
        instance.total_parking = validated_data.get('total_parking',instance.total_parking)
        instance.save()

        return instance
# //////////////////////////////////////////////// ZONES ////////////////////////////////////////////////


# //////////////////////////////////////////////// POSITIONS ////////////////////////////////////////////////
class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('position_id','position_name','is_avaliable','zone_id')

    def create(self, validated_data):
        return Position.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.position_name = validated_data.get('position_name',instance.position_name)
        instance.is_avaliable = validated_data.get('is_avaliable',instance.is_avaliable)
        instance.save()

        return instance
# //////////////////////////////////////////////// POSITIONS ////////////////////////////////////////////////