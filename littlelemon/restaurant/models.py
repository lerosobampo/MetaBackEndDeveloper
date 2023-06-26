from django.db import models

# Create your models here.
class Menu(models.Model):                      #MenuItem
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inventory = models.IntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    name = models.CharField(max_length=255)
    guests = models.IntegerField()             #No_of_guests
    bookingDate = models.DateField()

