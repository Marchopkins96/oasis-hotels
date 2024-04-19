from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from datetime import date
from django.utils import timezone
import json
from django.views import generic, View
from .forms import BookingForm
from .models import Hotel, Booking

class Home(generic.TemplateView):
    template_name = 'index.html'


def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'index.html', {'hotels': hotels})

def hotel_booking(request):
    all_hotels = Hotel.objects.all()
    paginator = Paginator(all_hotels, 6)  # Display 6 cabins per page
    page_number = request.GET.get('page')
    hotels = paginator.get_page(page_number)

    return render(request, 'hotel_booking.html', {'hotels': hotels})

@login_required
def booking_create(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.hotel = hotel
            booking.user = request.user

            num_guests = form.cleaned_data['num_guests']
            if num_guests <= 0:
                form.add_error('num_guests', "The number of guests must be greater than zero.")  # noqa
                messages.warning(request, "The number of guests must be greater than zero.")  # noqa
            elif num_guests > booking.hotel.max_guests:
                form.add_error('num_guests', "The number of guests entered exceeds the maximum allowed.")  # noqa
                messages.warning(request, "The number of guests entered exceeds the maximum amount allowed.")  # noqa
            else:
                check_in_date = form.cleaned_data['check_in_date']
                check_out_date = form.cleaned_data['check_out_date']
                today = timezone.now().date()

                if check_in_date < today:
                    form.add_error('check_in_date', "Please select a future check-in date.")  # noqa
                    messages.warning(request, "Please select a future check-in date.")  # noqa
                elif check_out_date < check_in_date:
                    form.add_error('check_out_date', "Check-out date cannot be earlier than the check-in date.")  # noqa
                    messages.warning(request, "Check-out date cannot be earlier than the check-in date.")  # noqa
                elif check_in_date == check_out_date:
                    form.add_error('check_out_date', "Check-out date cannot be the same as the check-in date.")  # noqa
                    messages.warning(request, "Check-out date cannot be the same as the check-in date.")  # noqa
                else:
                    # Check if the hotel is already booked for the selected dates  # noqa
                    existing_bookings = Booking.objects.filter(
                        hotel=hotel,
                        check_in_date__lte=check_out_date,
                        check_out_date__gte=check_in_date,
                    )
                    if existing_bookings.exists():
                        form.add_error(None, "The hotel is already booked for the selected dates.")  # noqa
                        messages.warning(request, "The hotel is already booked for the selected dates.")  # noqa
                    else:
                        booking.save()
                        messages.success(request, "New booking created successfully.")  # noqa
                        return redirect('booking_success', hotel_id=hotel.id, booking_id=booking.id)  # noqa   
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    if field != '__all__':
                        messages.warning(request, f"{form[field].label}: {error}")  # noqa
    else:
        form = BookingForm()

    booked_dates = Booking.objects.filter(hotel=hotel).values_list('check_in_date', 'check_out_date')  # noqa
    
    booked_dates_str = [[str(check_in_date), str(check_out_date)] for check_in_date, check_out_date in booked_dates]  # noqa

    context = {
        'hotel': hotel,
        'form': form,
        'booked_dates_json': json.dumps(booked_dates_str),
    }
    return render(request, 'my_booking.html', context)

@login_required
def booking_success(request, hotel_id, booking_id):
    cabin = get_object_or_404(Hotel, id=hotel_id)
    booking = get_object_or_404(Booking, id=booking_id)
    num_guests = booking.num_guests
    check_in_date = booking.check_in_date
    check_out_date = booking.check_out_date

    context = {'hotel': Hotel, 'booking': booking, 'num_guests': num_guests, 'check_in_date': check_in_date, 'check_out_date': check_out_date}  # noqa
    return render(request, 'booking_success.html', context)

@login_required
def booking_overview(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking_overview.html', {'bookings': bookings})

@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    context = {'form': None, 'booking': booking}

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            num_guests = form.cleaned_data['num_guests']
            if num_guests <= 0:
                form.add_error('num_guests', "The number of guests must be greater than zero.")  # noqa
                messages.warning(request, "The number of guests must be greater than zero.")  # noqa
            elif num_guests > booking.hotel.max_guests:
                form.add_error('num_guests', "The number of guests entered exceeds the maximum allowed")  # noqa
                messages.warning(request, "The number of guests entered exceeds the maximum amount allowed.")  # noqa
            else:
                check_in_date = form.cleaned_data['check_in_date']
                check_out_date = form.cleaned_data['check_out_date']
                today = timezone.now().date()
                if check_in_date < today:
                    form.add_error('check_in_date', "Please select a future check-in date.")  # noqa
                    messages.warning(request, "Please select a future check-in date.")  # noqa
                elif check_out_date < check_in_date:
                    form.add_error('check_out_date', "Check-out date cannot be earlier than the check-in date.")  # noqa
                    messages.warning(request, "Check-out date cannot be earlier than the check-in date.")  # noqa
                elif check_in_date == check_out_date:
                    form.add_error('check_out_date', "Check-out date cannot be the same as the check-in date.")  # noqa
                    messages.warning(request, "Check-out date cannot be the same as the check-in date.")  # noqa
                else:
                    overlapping_bookings = booked_dates.filter(
                        check_in_date__lte=check_out_date,
                        check_out_date__gte=check_in_date
                    )

                    if overlapping_bookings.exists():
                        form.add_error(None, "The hotel is already booked for the selected dates.")  # noqa
                        messages.warning(request, "The hotel is already booked for the selected dates.")  # noqa
                    else:
                        form.save()
                        messages.success(request, "Booking updated successfully.")  # noqa
                        return redirect('booking_overview')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    if field != '__all__':
                        messages.warning(request, f"{form[field].label}: {error}")  # noqa
    else:
        form = BookingForm(instance=booking)
    
    booked_dates = booked_dates.values_list('check_in_date', 'check_out_date')
    booked_dates_str = [[str(check_in_date), str(check_out_date)] for check_in_date, check_out_date in booked_dates]  # noqa

    context = {
        'form': form,
        'booking': booking,
        'booked_dates': booked_dates,
        'booked_dates_json': json.dumps(booked_dates_str),
    }
    
    return render(request, 'edit_booking.html', context)

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking deleted successfully.")
        return redirect('booking_overview')

    return render(request, 'delete_booking.html', {'booking': booking})
