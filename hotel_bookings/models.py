from django.db import models
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.

class Extras(models.Model):
    """
    Add a new Extra as Admin in admin panel
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    """
    Add a new hotel as Admin in admin panel
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('log_hotel_images')
    max_guests = models.PositiveIntegerField(default=1)
    rooms = models.PositiveIntegerField(default=1)
    extras = models.ManyToManyField(Extras)

    def __str__(self):
        return self.name

class Booking(models.Model):
    """
    Hotel Booking
    This class handles the information related to a booking made by a user
    for a specific hotel. It stores details such as the booked hotel,
    the user who made the booking, check-in and check-out dates,
    the number of guests, optional quantities of breakfasts and kids club tickets

    """
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_guests = models.PositiveIntegerField(default=1)
    breakfast_included = models.PositiveIntegerField(default=0, null=True)
    kids_club_tickets = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return f"Booking {self.id} - Hotel: {self.hotel.name}, User: {self.user.username}"  # noqa