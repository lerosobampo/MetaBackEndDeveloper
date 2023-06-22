from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inventory = models.IntegerField()

class Booking(models.Model):
    name = models.CharField(max_length=255)
    guests = models.IntegerField()             #No_of_guests
    bookingDate = models.DateField()

