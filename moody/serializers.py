from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers

from .models import Users, Moods


class UsersSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        geo_field = 'geom'


class MoodsSerializer(GeoFeatureModelSerializer):
    distance = serializers.CharField()

    class Meta:
        model = Moods
        fields = '__all__'
        geo_field = 'geom'
        read_only_fields = ['distance']
