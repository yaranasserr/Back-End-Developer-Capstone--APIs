from django.test import TestCase, RequestFactory
from restuarant.views import MenuItemView 
from restuarant.models import Menu
from restuarant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(name='Menu 1', price=10.0)
        self.menu2 = Menu.objects.create(name='Menu 2', price=15.0)

    def test_getall(self):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

# class MenuViewTest(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         Menu.objects.create(
#             title="Rice",
#             price=10,
#             inventory=50
#         )
#         Menu.objects.create(
#             title="Bulgur",
#             price=25,
#             inventory=100
#         )
    
#     def test_getall(self):
#         items = Menu.objects.all()
#         serialized_items = MenuSerializer(items, many=True)
#         request = self.factory.get('restaurant/menu/items/')
#         response = MenuItemsView.as_view()(request)
#         self.assertEqual(response.data, serialized_items.data)
