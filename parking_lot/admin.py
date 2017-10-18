from django.contrib import admin

from .models import Car, ParkingSpace, ParkingLot

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass

@admin.register(ParkingLot)
class ParkingLotAdmin(admin.ModelAdmin):
    pass

@admin.register(ParkingSpace)
class ParkingSpaceAdmin(admin.ModelAdmin):
    pass
