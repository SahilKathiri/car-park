from django import forms
from django.contrib.admin import widgets

from .models import ParkingLot, ParkingSpace, Car

class AddCarForm(forms.ModelForm):
    parking_space = forms.ModelChoiceField(queryset=ParkingSpace.objects.filter(occupied=False))

    def __init__(self, *args, **kwargs):
        super(AddCarForm, self).__init__(*args, **kwargs)
        self.fields["parking_space"].widget.attrs['style'] = 'display: block'


    class Meta:
        model = Car
        exclude = ['out_time']


class RemoveCarForm(forms.Form):
    car = forms.ModelChoiceField(queryset=Car.objects.all())
    out_time = forms.SplitDateTimeField()

    def __init__(self, *args, **kwargs):
        super(RemoveCarForm, self).__init__(*args, **kwargs)
        self.fields["car"].widget.attrs['style'] = 'display: block'
