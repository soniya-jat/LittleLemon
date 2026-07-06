from django.test import TestCase
from rest_framework.test import APIClient

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
	def setUp(self):
		self.client = APIClient()
		Menu.objects.create(name="IceCream", price="80.00", inventory=100)
		Menu.objects.create(name="Cake", price="120.00", inventory=50)
		Menu.objects.create(name="Pizza", price="300.00", inventory=20)

	def test_getall(self):
		response = self.client.get("/restaurant/menu/items/")
		menus = Menu.objects.all().order_by("id")
		serialized_data = MenuSerializer(menus, many=True).data

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json(), serialized_data)
