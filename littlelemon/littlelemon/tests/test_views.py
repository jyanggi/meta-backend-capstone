
from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework import status
from restaurant.models import Menu, Booking
from django.utils import timezone



class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@littlelemon.com'
        )

        self.items = [Menu.objects.create(
            title='Item1', price=12.99, inventory=10), Menu.objects.create(
            title='Item2', price=12.99, inventory=10), Menu.objects.create(
            title='Item3', price=12.99, inventory=10)]

    def login(self):
        self.client.login(username='testuser', password='testpassword')

    def test_view_authentication(self):
        response = self.client.get('/api/menu', follow=True)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.login()
        response = self.client.get('/api/menu', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getall(self):
        self.login()
        response = self.client.get('/api/menu', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # pagination size in settings.py set to 2
        self.assertEqual(len(response.data['results']), 2)


class BookingViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@littlelemon.com'
        )
        the_date = timezone.now()

        self.items = [Booking.objects.create(name="Name1", no_of_guests=1, booking_date=the_date, reservation_slot=1),
                      Booking.objects.create(
                          name="Name2", no_of_guests=2, booking_date=the_date, reservation_slot=2),
                      Booking.objects.create(
                          name="Name3", no_of_guests=3, booking_date=the_date, reservation_slot=3)
                      ]

    def login(self):
        self.client.login(username='testuser', password='testpassword')

    def test_view_authentication(self):
        response = self.client.get('/api/booking', follow=True)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.login()
        response = self.client.get('/api/booking', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getall(self):
        self.login()
        response = self.client.get('/api/booking', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # pagination size in settings.py set to 2
        self.assertEqual(len(response.data['results']), 2)
