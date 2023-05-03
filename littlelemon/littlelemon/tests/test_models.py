
from restaurant.models import Menu, Booking
from django.test import TestCase
from datetime import datetime

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name="Name", no_of_guests=2, booking_date= datetime.now(), reservation_slot= 12)
        self.assertEqual(str(item), "Name")