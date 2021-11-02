from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers

from .models import Users, Locations, Moods


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name']


class LocationsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'
        geo_field = 'poly'


class MoodsSerializer(GeoFeatureModelSerializer):
    distance = serializers.CharField()

    class Meta:
        model = Moods
        fields = '__all__'
        geo_field = 'geom'
        read_only_fields = ['distance']
