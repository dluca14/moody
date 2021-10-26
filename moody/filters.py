from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter
from django_filters import filters
from .models import Users, Moods


class MoodProximityFilter(GeoFilterSet):
    home_mood = filters.CharFilter(method='get_moods_by_user_home')
    office_mood = filters.CharFilter(method='get_moods_by_user_office')

    class Meta:
        model = Users
        exclude = ['geom']

    def get_moods_by_user_home(self, queryset, name):
        query_ = Moods.objects.filter(pk=name)
        if query_:
            obj = query_.first()
            return queryset.filter(geom__within=obj.geom)
        return queryset

    def get_moods_by_user_office(self, queryset, name):
        query_ = Moods.objects.filter(pk=name)
        if query_:
            obj = query_.first()
            return queryset.filter(geom__within=obj.geom)
        return queryset
