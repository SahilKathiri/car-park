import datetime

from django import forms
from django.shortcuts import render, redirect

from .models import Car, ParkingLot, ParkingSpace

from .forms import AddCarForm, RemoveCarForm

def index(request):

    if request.method == 'POST':
        if 'add_car' in request.POST:
            add_car_form = AddCarForm(request.POST)
            if add_car_form.is_valid():
                car = add_car_form.save()
                car.save()
                car.parking_space.occupied = True
                car.parking_space.save()
                return redirect('parking_lot:index')
        elif 'remove_car' in request.POST:
            remove_car_form = RemoveCarForm(request.POST)
            if remove_car_form.is_valid():
                car = remove_car_form.cleaned_data['car']
                car.out_time = remove_car_form.cleaned_data['out_time']
                car.parking_space.occupied = False
                car.parking_space.save()
                car.parking_space = None
                car.save()

                time_diff = car.out_time - car.in_time
                if time_diff < datetime.timedelta(hours=3):
                    price = 10
                elif time_diff < datetime.timedelta(hours=4):
                    price = 20
                else:
                    price = 40
                result_dict = {}
                result_dict['price'] = price
                result_dict['car'] = car
                return render(request, 'parking_lot/result.html', result_dict)

    add_car_form = AddCarForm()
    remove_car_form = RemoveCarForm()

    context_dict = {}
    context_dict['slots_available'] = ParkingSpace.objects.filter(occupied=False).count()
    context_dict['add_car_form'] = add_car_form
    context_dict['remove_car_form'] = remove_car_form
    context_dict['occupied_spaces'] = Car.objects.filter(parking_space__isnull=False)
    context_dict['vacant_spaces'] = ParkingSpace.objects.filter(occupied=False)
    context_dict['free_space'] = ParkingSpace.objects.filter(occupied=False).count()
    return render(request, 'parking_lot/index.html', context_dict)

def car_stats(request):
    context_dict = {}
    context_dict['total_cars'] = Car.objects.all().count()
    context_dict['cars'] = Car.objects.all()
    return render(request, 'parking_lot/cars.html', context_dict)
