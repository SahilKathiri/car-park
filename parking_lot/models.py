from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class ParkingLot(models.Model):
    lot_name = models.CharField(max_length=50)
    total_spaces = models.IntegerField()    # per floor
    total_floors = models.IntegerField()

    def __str__(self):
        return self.lot_name

@receiver(post_save, sender=ParkingLot)
def add_parking_spaces(sender, instance, *args, **kwargs):
    spaces = instance.total_spaces
    floors = instance.total_floors
    lot_name = instance.lot_name

    for f in range(floors):
        for s in range(spaces):
            if not ParkingSpace.objects.filter(space=s+1, level=chr(65 + f), parking_lot=instance):
                parking_space = ParkingSpace.objects.create(space=s+1, level=chr(65 + f), parking_lot=instance)
                parking_space.save()

class ParkingSpace(models.Model):
    space = models.IntegerField()
    level = models.CharField(max_length=1)
    parking_lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return "{0}{1}".format(self.level, self.space)

class Car(models.Model):
    license_no = models.CharField(max_length=6, unique=True)
    in_time = models.DateTimeField(auto_now_add=True)
    out_time = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    parking_space = models.OneToOneField(ParkingSpace, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}".format(self.license_no)
