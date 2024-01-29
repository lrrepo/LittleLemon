from django.test import TestCase
from restaurant.models import Menu
from restaurant.views import MenuItemsView

class MenuViewTest(TestCase):
    def setUpMenu(cls):
        Menu.objects.create(Title="IceCream", Price=80, Inventory=100),
        Menu.objects.create(Title="GreekSalad", Price=50, Inventory=60),
        Menu.objects.create(Title="SeafoodPasta", Price=70, Inventory=70)
        
    def test_getall(self):
        menuitems = MenuItemsView.serializer_class.data
        menuitems = [{"IceCream":"80"}, {"GreekSalad":"50"}, {"SeafoodPasta":"70"}]
        self.assertEqual(menuitems, [{"IceCream":"80"}, {"GreekSalad":"50"}, {"SeafoodPasta":"70"}])
        