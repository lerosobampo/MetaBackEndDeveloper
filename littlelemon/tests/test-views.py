from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of Menu
        self.menu1 = Menu.objects.create(name='Menu 1', price=10)
        self.menu2 = Menu.objects.create(name='Menu 2', price=15)
        self.menu3 = Menu.objects.create(name='Menu 3', price=20)

    def test_getall(self):
        client = APIClient()
        url = reverse('menu-list')  # Replace 'menu-list' with your actual URL name

        # Perform GET request
        response = client.get(url)

        # Retrieve all Menu objects and serialize them
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Assert response status code
        self.assertEqual(response.status_code, 200)

        # Assert serialized data
        self.assertEqual(response.data, serializer.data)