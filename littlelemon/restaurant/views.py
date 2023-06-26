from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Menu, Booking
from django.contrib.auth.models import User
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.decorators import permission_classes

# Create your views here.
#def sayHello(request):
 #return HttpResponse('Hello World')

def index(request):
 return render(request, 'index.html', {})

class MenuItemsView(ListCreateAPIView):
 permission_classes = [IsAuthenticated]  #Random
 queryset = Menu.objects.all()
 serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
 queryset = Menu.objects.all()
 serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
 queryset = Booking.objects.all()
 serializer_class = BookingSerializer
 permission_classes = [IsAuthenticated]

class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated]


