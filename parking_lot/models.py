from django.db import models



class ParkingLot(models.Model):
    lot_name = models.CharField(max_length=50)
    total_spaces = models.IntegerField()    # per floor
    total_floors = models.IntegerField()

    def __str__(self):
        return self.lot_name

class ParkingSpace(models.Model):
    space = models.IntegerField()
    level = models.CharField(max_length=1)
    parking_lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}{1} - Lot: {2}".format(self.level, self.space, self.parking_lot)

class Car(models.Model):
    license_no = models.CharField(max_length=6, unique=True)
    in_time = models.DateTimeField(auto_now_add=True)
    out_time = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    parking_space = models.OneToOneField(ParkingSpace, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1}".format(self.license_no, self.parking_space)
