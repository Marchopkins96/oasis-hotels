from . import views
from django.urls import path

urlpatterns = [
    path('', views.hotel_list, name='home'),
    path('hotel-booking/', views.hotel_booking, name='hotel_booking'),
]