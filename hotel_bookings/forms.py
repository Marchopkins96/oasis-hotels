from django import forms
from .models import Booking, Extras
from django.core.validators import MinValueValidator


class BookingForm(forms.ModelForm):
    """
    A form for creating or updating a booking.
    This form is used for creating or updating a booking
    The form includes validators to ensure that the minimum value
    for num_guests,breakfast_included, and kids_club_tickets is 0 or value chosen by user.
    """
    num_guests = forms.IntegerField(validators=[MinValueValidator(1)])
    # Optional field for breakfast included
    breakfast_included = forms.IntegerField(
        validators=[MinValueValidator(0)], required=False)
    # Optional field for kids club tickets
    kids_club_tickets = forms.IntegerField(
        validators=[MinValueValidator(0)], required=False)

    class Meta:
        model = Booking
        fields = ['check_in_date',
                  'check_out_date',
                  'num_guests',
                  'breakfast_included',
                  'kids_club_tickets']
