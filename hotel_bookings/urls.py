from . import views
from django.urls import path

urlpatterns = [
    # Open Home page
    path('', views.hotel_list, name='home')
]