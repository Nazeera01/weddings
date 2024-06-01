from django import forms

from .models import Client, Event, Vendor, Venue


class ClientModelform(forms.ModelForm):
    class Meta:
        model= Client
        fields='__all__'

class EventModelform(forms.ModelForm):
    class Meta:
        model= Event
        fields='__all__'
        exclude= ['image','schedule','description']


class VendorModelform(forms.ModelForm):
    class Meta:
        model= Vendor
        fields='__all__'


class VenueModelform(forms.ModelForm):
    class Meta:
        model= Venue
        fields='__all__'
        exclude=['image']


