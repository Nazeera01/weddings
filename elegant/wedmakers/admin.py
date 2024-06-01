from django.contrib import admin
from .models import Client, Vendor, Venue, Event
# Register your models here.

admin.site.register(Client)
admin.site.register(Vendor)
admin.site.register(Venue)
admin.site.register(Event)
