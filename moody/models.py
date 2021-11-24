from django.contrib.gis.db import models


class Image(models.Model):
    image_url = models.ImageField(upload_to='static/bills', blank=True)


class Users(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)


class Locations(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    poly = models.PolygonField()

    user = models.ForeignKey(Users, related_name='locations', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
# from django.contrib.gis.geos import GEOSGeometry, Point
# polygon = GEOSGeometry('POLYGON ((-98.503358 29.335668, -98.503086 29.335668, -98.503086 29.335423, -98.503358 29.335423, -98.503358 29.335668))', srid=4326)
# point = Point(-98.503259, 29.335569, srid=4326)


class Moods(models.Model):
    picture_name = models.CharField(max_length=255)
    mood_addr = models.PointField(null=False)
    type = models.CharField(max_length=255)

    location = models.ForeignKey(Locations, related_name='moods', on_delete=models.CASCADE)
    user = models.ForeignKey(Users, related_name='moods', on_delete=models.CASCADE)
