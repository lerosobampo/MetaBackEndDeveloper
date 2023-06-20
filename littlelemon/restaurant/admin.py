from django.contrib import admin
from .models import Menu     #TABLE IMPORT
from .models import Booking  #TABLE IMPORT

# Register your models here.
admin.site.register(Menu)       #TABLE REGISTER
admin.site.register(Booking)    #TABLE REGISTER
