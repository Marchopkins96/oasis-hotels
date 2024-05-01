from . import views
from django.urls import path
from django.conf.urls import handler404
from django.conf.urls import handler500
from .views import custom_handler404, custom_handler500

#URLs list
urlpatterns = [
    # Open Home and Contact page
    path('', views.hotel_list, name='home'),
    path('contact/', views.contact_view, name='contact'),

    # Create, Read, Update and Delete Hotel Bookings
    path('hotel-booking/', views.hotel_booking, name='hotel_booking'),
    path('booking/<int:hotel_id>/', views.booking_create, name='my_booking'),
    path('booking/success/<int:hotel_id>/<int:booking_id>/', views.booking_success, name='booking_success'),
    path('booking-overview/', views.booking_overview, name='booking_overview'),
    path('booking/edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('booking/<int:booking_id>/delete/', views.delete_booking, name='delete_booking'),
]

handler404 = custom_handler404
handler500 = custom_handler500