from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from datetime import date
from django.utils import timezone
import json
from django.views import generic, View
from .forms import BookingForm
from .models import Hotel, Booking, Extras

class Home(generic.TemplateView):
    template_name = 'index.html'

def contact_view(request):
    return render(request, 'contact.html')


def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'index.html', {'hotels': hotels})

def hotel_booking(request):
    all_hotels = Hotel.objects.all().prefetch_related('extras')
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
                form.add_error(
                    'num_guests',
                     "The number of guests must be greater than zero."
                )
                messages.warning(
                    request, 
                    "The number of guests must be greater than zero."
                )
            elif num_guests > booking.hotel.max_guests:
                form.add_error('num_guests',
                "The number of guests entered exceeds the maximum allowed."
                )
                messages.warning(
                    request,
                    "The number of guests entered exceeds the maximum amount allowed."
                )
            else:
                check_in_date = form.cleaned_data['check_in_date']
                check_out_date = form.cleaned_data['check_out_date']
                today = timezone.now().date()

                if check_in_date < today:
                    form.add_error(
                        'check_in_date',
                        "Please select a future check-in date."
                    )
                    messages.warning(
                        request,
                        "Please select a future check-in date."
                    )
                elif check_out_date < check_in_date:
                    form.add_error(
                        'check_out_date',
                        "Check-out date cannot be earlier than the check-in date."
                    )
                    messages.warning(
                        request,
                        "Check-out date cannot be earlier than the check-in date."
                    )
                elif check_in_date == check_out_date:
                    form.add_error(
                        'check_out_date',
                        "Check-out date cannot be the same as the check-in date."
                    )
                    messages.warning(
                        request,
                        "Check-out date cannot be the same as the check-in date."
                    )
                else:
                    existing_bookings = Booking.objects.filter(
                        hotel=hotel,
                        check_in_date__lte=check_out_date,
                        check_out_date__gte=check_in_date,
                    )
                    if existing_bookings.exists():
                        form.add_error(
                            None,
                            "The hotel is already booked for the selected dates."
                        )
                        messages.warning(
                            request,
                            "The hotel is already booked for the selected dates."
                        )
                    else:
                        breakfast_included = form.cleaned_data.get(
                                                   'breakfast_included')
                        kids_club_tickets = form.cleaned_data.get('kids_club_tickets')

                        if breakfast_included and breakfast_included < 0:  # noqa
                            form.add_error(
                                'breakfast_included',
                                "Breakfast included cannot be negative."
                            )
                            messages.warning(
                                request,
                                "Breakfast included cannot be negative."
                            )

                        if kids_club_tickets and kids_club_tickets < 0:
                            form.add_error(
                                'kids_club_tickets',
                                "The number of kids club tickets cannot be negative."
                            )
                            messages.warning(
                                request,
                                "The number of kids club tickets cannot be negative."
                            )

                        if not form.errors:
                            booking.save()
                            messages.success(
                                request,
                                "New booking created successfully."
                            )
                            return redirect(
                                'booking_success',
                                hotel_id=hotel.id, booking_id=booking.id
                            )
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    if field != '__all__':
                        messages.warning(
                            request,
                            f"{form[field].label}: {error}"
                        )
    else:             
        form = BookingForm()

    booked_dates = Booking.objects.filter(hotel=hotel).values_list(
        'check_in_date',
        'check_out_date'
    )
    
    booked_dates_str = [
        [str(check_in_date), str(check_out_date)]
        for check_in_date, check_out_date in booked_dates
    ]

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
    breakfast_included = booking.breakfast_included
    kids_club_tickets = booking.kids_club_tickets

    context = {
        'hotel': Hotel,
        'booking': booking,
        'num_guests': num_guests,
        'check_in_date': check_in_date,
        'check_out_date': check_out_date,
        'breakfast_included': breakfast_included,
        'kids_club_tickets': kids_club_tickets,
    }
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
        form = form = BookingForm(request.POST, instance=booking, initial={
            'breakfast_included': booking.breakfast_included,
            'kids_club_tickets': booking.kids_club_tickets,
        })
        if form.is_valid():
            num_guests = form.cleaned_data['num_guests']
            if num_guests <= 0:
                form.add_error(
                    'num_guests',
                    "The number of guests must be greater than zero.")
                messages.warning(
                    request,
                    "The number of guests must be greater than zero.")
            elif num_guests > booking.hotel.max_guests:
                form.add_error(
                    'num_guests',
                    "The number of guests entered exceeds the maximum allowed")
                messages.warning(
                    request,
                    "The number of guests entered exceeds the maximum amount allowed.")
            else:
                check_in_date = form.cleaned_data['check_in_date']
                check_out_date = form.cleaned_data['check_out_date']
                today = timezone.now().date()
                if check_in_date < today:
                    form.add_error(
                        'check_in_date',
                        "Please select a future check-in date.")
                    messages.warning(
                        request,
                        "Please select a future check-in date.")
                elif check_out_date < check_in_date:
                    form.add_error(
                        'check_out_date',
                        "Check-out date cannot be earlier than the check-in date.")
                    messages.warning(
                        request,
                        "Check-out date cannot be earlier than the check-in date.")
                    form.add_error(
                        'check_out_date',
                        "Check-out date cannot be the same as the check-in date.")
                    messages.warning(
                        request,
                        "Check-out date cannot be the same as the check-in date.")
                else:
                    overlapping_bookings = booked_dates.filter(
                        check_in_date__lte=check_out_date,
                        check_out_date__gte=check_in_date
                    )

                    if overlapping_bookings.exists():
                        form.add_error(
                            None,
                            "The hotel is already booked for the selected dates.")
                        messages.warning(
                            request,
                            "The hotel is already booked for the selected dates.")
                    else:
                        breakfast_included = form.cleaned_data.get(
                                                   'breakfast_included')
                        kids_club_tickets = form.cleaned_data.get('kids_club_tickets')
                        if breakfast_included and (
                           breakfast_included <
                           0 or breakfast_included > num_guests):
                            form.add_error(
                                'breakfast_included',
                                "Invalid number of breakfasts included."
                            )
                            messages.warning(
                                request,
                                "Invalid number of breakfasts included."
                            )

                        if kids_club_tickets and (
                           kids_club_tickets < 0 or kids_club_tickets > 10):
                            form.add_error(
                                'kids_club_tickets',
                                "Number of kids club tickets can't be negative."
                            )
                            messages.warning(
                                request,
                                "Number of kids club tickets can't be negative."
                            )

                        if not form.errors:
                            form.save()
                            messages.success(
                                request,
                                "Booking updated successfully."
                            )
                            return redirect('booking_overview')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    if field != '__all__':
                        messages.warning(
                            request,
                            f"{form[field].label}: {error}")
    else:
        form = BookingForm(instance=booking)
    
    booked_dates = booked_dates.values_list('check_in_date', 'check_out_date')
    booked_dates_str = [[str(check_in_date),
                        str(check_out_date)] for check_in_date,
                        check_out_date in booked_dates]

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
