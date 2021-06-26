from rest_framework import serializers
from .models import Area
from .models import Point


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'name')


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ('id', 'name', 'description', 'longitude', 'latitude', 'fill_type', 'color', 'angle', 'area')
        read_only_fields = ('id', )
