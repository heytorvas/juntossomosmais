from django.db import models

class Name(models.Model):
    title = models.CharField(max_length=3)
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)

class Coordinates(models.Model):
    latitude = models.FloatField(max_length=15)
    longitude = models.FloatField(max_length=15)

class Timezone(models.Model):
    offset = models.CharField(max_length=8)
    description = models.CharField(max_length=40)

class Location(models.Model):
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    postcode = models.IntegerField(max_length=5)
    coordinates = models.OneToOneField(Coordinates)
    timezone = models.OneToOneField(Timezone)

class Picture(models.Model):
    large = models.URLField()
    medium = models.URLField()
    thumbnail = models.URLField()

class User(models.Model):
    type = models.CharField(max_length=10)
    gender = models.CharField(max_length=1)
    name = models.OneToOneField(Name)
    location = models.OneToOneField(Location)
    email = models.EmailField()
    birthday = models.DateTimeField()
    registered = models.DateTimeField()
    picture = models.OneToOneField(Picture)
    nationality = models.CharField(max_length=2)
