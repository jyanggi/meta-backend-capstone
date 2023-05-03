
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from . import views

router: DefaultRouter = DefaultRouter(trailing_slash=False)
router.register(r'booking', views.BookingViewSet)
router.register(r'menu', views.MenuItemsView)

urlpatterns = [
    # PAGE VIEWS
    path('', views.index, name='home'),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('reservations/', views.reservations, name="reservations"),
    path('bookings', views.bookings, name='bookings'),
    path('book/', views.book, name="book"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    # API

    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]
