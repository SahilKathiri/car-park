import datetime

from django import forms
from django.shortcuts import render, redirect

from .models import Car, ParkingLot

def index(request):
    return render(request, 'parking_lot/index.html', {})
