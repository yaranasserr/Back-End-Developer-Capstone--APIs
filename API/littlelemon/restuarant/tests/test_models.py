from django.test import TestCase
from restuarant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        # create a new menu object
        item = MenuItem.objects.create(Title='pasta', price=5, inventory=12)
        
        self.assertEqual(item,'pasta:12')

        # check that the string representation of the object is as expected
        # self.assertEqual(str(menu), 'Breakfast : A selection of breakfast items')

        # check that the name, price, and description fields are set correctly
        # self.assertEqual(menu.name, 'Breakfast')
        # self.assertEqual(menu.price, 20)
        # self.assertEqual(menu.description, 'A selection of breakfast items')

        # check that the calculate_total_cost method works correctly
       