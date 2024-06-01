from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=100)
    groom_name = models.CharField(max_length=100)
    bride_name=models.CharField(max_length=100)
    address = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    wedding_date = models.DateField()
    preferences = models.TextField(blank=True)



class Vendor(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    services = models.TextField()
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='vendor_pics/', null=True, blank=True)

class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='venue_pics/', null=True, blank=True)
    description = models.TextField(blank=True)



class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    guest_list = models.TextField()
    schedule = models.TextField()
    image = models.ImageField(upload_to='event_pics/', null=True, blank=True)
    description = models.TextField(blank=True)


# Create your models here.
