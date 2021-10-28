from django.contrib.gis.db import models


class Users(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    # addr_home = models.PolygonField()
    # addr_office = models.PolygonField()

    class Meta:
        managed = False
        db_table = 'users'


class UserLocations(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    mpoly = models.MultiPolygonField()

    user_id = models.ForeignKey(Users, related_name='locations', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Moods(models.Model):
    picture_name = models.CharField(max_length=255)
    location = models.PointField(null=False)
    type = models.CharField(max_length=255)

    user_id = models.ForeignKey(Users, related_name='moods', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'moods'
