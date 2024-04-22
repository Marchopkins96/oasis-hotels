from . import views
from django.urls import path

urlpatterns = [
    path('', views.hotel_list, name='home'),
    path('hotel-booking/', views.hotel_booking, name='hotel_booking'),
    path('booking/<int:hotel_id>/', views.booking_create, name='my_booking'),  # noqa
    path('booking/success/<int:hotel_id>/<int:booking_id>/', views.booking_success, name='booking_success'),  # noqa
    path('booking-overview/', views.booking_overview, name='booking_overview'),
    path('booking/edit/<int:booking_id>/', views.edit_booking, name='edit_booking'), # noqa
    path('booking/<int:booking_id>/delete/', views.delete_booking, name='delete_booking'),  # noqa
    path('contact/', views.contact_view, name='contact'),
]