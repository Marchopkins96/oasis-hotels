from django import forms
from .models import Booking, Extras
from django.core.validators import MinValueValidator


class BookingForm(forms.ModelForm):
    num_guests = forms.IntegerField(validators=[MinValueValidator(1)])
    breakfast_included = forms.IntegerField(validators=[MinValueValidator(0)], required=False)
    kids_club_tickets = forms.IntegerField(validators=[MinValueValidator(0)], required=False)

    class Meta:
        model = Booking
        fields = ['check_in_date',
                  'check_out_date',
                  'num_guests',
                  'breakfast_included',
                  'kids_club_tickets']