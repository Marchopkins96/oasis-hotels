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
    """
    This function retrieves all hotels from the database and renders
    the 'index.html' template, passing the hotels as context.
    """
    hotels = Hotel.objects.all()
    return render(request, 'index.html', {'hotels': hotels})

def hotel_booking(request):
    """
    This function retrieves all hotles from the database with
    prefetched extras, paginates the hotles to display 6 per page,
    and renders the 'hotel_booking.html' template,
    passing the paginated hotels as context.
    """
    all_hotels = Hotel.objects.all().prefetch_related('extras')
    paginator = Paginator(all_hotels, 6)  # Display 6 cabins per page
    page_number = request.GET.get('page')
    hotels = paginator.get_page(page_number)

    return render(request, 'hotel_booking.html', {'hotels': hotels})

@login_required
def booking_create(request, hotel_id):
    """
    This function handles the creation of a new booking for the
    specified hotel. It performs form validation, checks for validation
    errors, and handles various validation cases. If the booking is
    successfully created, it redirects to the booking success page.
    """
    hotel = Hotel.objects.get(id=hotel_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Process form data and perform validations
            booking = form.save(commit=False)
            booking.hotel = hotel
            booking.user = request.user

            num_guests = form.cleaned_data['num_guests']
            # Check if the number of guests is greater than zero
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
                # Check if the number of guests exceeds the maximum allowed
                form.add_error(
                    'num_guests',
                    "Exceeds maximum guests allowed."
                )
                messages.warning(
                    request,
                    "Exceeds maximum guests allowed."
                )
            else:
                check_in_date = form.cleaned_data['check_in_date']
                check_out_date = form.cleaned_data['check_out_date']
                today = timezone.now().date()

                if check_in_date < today:
                    # Check if the check-in date is in the past
                    form.add_error(
                        'check_in_date',
                        "Please select a future check-in date."
                    )
                    messages.warning(
                        request,
                        "Please select a future check-in date."
                    )
                elif check_out_date < check_in_date:
                    # Check if check-out date is earlier than the check-in date
                    form.add_error(
                        'check_out_date',
                        "Check-out date can't be earlier than check-in date."
                    )
                    messages.warning(
                        request,
                        "Check-out date can't be earlier than check-in date."
                    )
                elif check_in_date == check_out_date:
                    # Check if check-in date and check-out date are the same
                    form.add_error(
                        'check_out_date',
                        "Check-out date can't be the same as check-in date."
                    )
                    messages.warning(
                        request,
                        "Check-out date can't be the same as check-in date."
                    )
                else:
                    # Check if there are any overlapping bookings
                    existing_bookings = Booking.objects.filter(
                        hotel=hotel,
                        check_in_date__lte=check_out_date,
                        check_out_date__gte=check_in_date,
                    )
                    if existing_bookings.exists():
                        form.add_error(
                            None,
                            "Hotel already booked for the selected dates"
                        )
                        messages.warning(
                            request,
                            "Hotel already booked for the selected dates"
                        )
                    else:
                        # Check additional validations
                        breakfast_included = form.cleaned_data.get(
                                                   'breakfast_included')
                        kids_club_tickets = form.cleaned_data.get('kids_club_tickets')

                        if breakfast_included and breakfast_included < 0:  # noqa
                            form.add_error(
                                'breakfast_included',
                                "Breakfast included can't be negative."
                            )
                            messages.warning(
                                request,
                                "Breakfast included can't be negative."
                            )
                        if breakfast_included and (
                           breakfast_included <
                           0 or breakfast_included > num_guests):
                            form.add_error(
                                'breakfast_included',
                                "Breakfast included cannot be greater than amount of guests."
                            )
                            messages.warning(
                                request,
                                "Breakfast included cannot be greater than amount of guests."
                            )

                        if kids_club_tickets and kids_club_tickets < 0:
                            form.add_error(
                                'kids_club_tickets',
                                "Number of kids club tickets can't be negative."
                            )
                            messages.warning(
                                request,
                                "Number of kids club tickets can't be negative."
                            )

                        if not form.errors:
                            booking.save()
                            messages.success(
                                request,
                                "New booking created successfully."
                            )
                            return redirect(
                                'booking_success',
                                hotel_id=hotel.id,
                                booking_id=booking.id
                            )
        else:
            # Handle form validation errors
            for field, errors in form.errors.items():
                for error in errors:
                    if field != '__all__':
                        messages.warning(
                            request,
                            f"{form[field].label}: {error}"
                        )
    else:
        form = BookingForm()
    # Get booked dates for the hotel
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
    """
    This function retrieves the hotel and booking objects associated
    with the provided IDs. It gathers the necessary information from
    the booking object. Finally, it renders the 'booking_success.html'
    template, passing the relevant context.
    """
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
    """
    This function retrieves all bookings associated with the currently
    logged-in user. It renders the 'booking_overview.html' template,
    passing the bookings as context.
    """
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking_overview.html', {'bookings': bookings})

@login_required
def edit_booking(request, booking_id):
    """
    This function handles the editing of an existing booking identified
    by the provided booking_id. It performs form validation, checks for
    validation errors, and handles various validation cases. If the
    booking is successfully updated, it redirects to the booking overview page.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booked_dates = Booking.objects.filter(
        hotel=booking.hotel).exclude(id=booking_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking, initial={
            'breakfast_included': booking.breakfast_included,
            'kids_club_tickets': booking.kids_club_tickets,
        })
        if form.is_valid():
            # Process form data and perform validations
            num_guests = form.cleaned_data['num_guests']
            if num_guests <= 0:
                # Check if the number of guests is greater than zero
                form.add_error(
                    'num_guests',
                    "The number of guests must be greater than zero.")
                messages.warning(
                    request,
                    "The number of guests must be greater than zero.")
            elif num_guests > booking.hotel.max_guests:
                # Check if the number of guests exceeds the maximum allowed
                form.add_error(
                    'num_guests',
                    "Exceeds maximum guests allowed.")
                messages.warning(
                    request,
                    "Exceeds maximum guests allowed.")
            else:
                check_in_date = form.cleaned_data['check_in_date']
                check_out_date = form.cleaned_data['check_out_date']
                today = timezone.now().date()
                if check_in_date < today:
                    # Check if the check-in date is in the past
                    form.add_error(
                        'check_in_date',
                        "Please select a future check-in date.")
                    messages.warning(
                        request,
                        "Please select a future check-in date.")
                elif check_out_date < check_in_date:
                    # Check if check-out date is earlier than the check-in date
                    form.add_error(
                        'check_out_date',
                        "Check-out date can't be earlier than check-in date.")
                    messages.warning(
                        request,
                        "Check-out date can't be earlier than check-in date.")
                elif check_in_date == check_out_date:
                    # Check if check-in date and check-out date are the same
                    form.add_error(
                        'check_out_date',
                        "Check-out date can't be the same as check-in date.")
                    messages.warning(
                        request,
                        "Check-out date can't be the same as check-in date.")
                else:
                    # Check if there are any overlapping bookings
                    overlapping_bookings = booked_dates.filter(
                        check_in_date__lte=check_out_date,
                        check_out_date__gte=check_in_date
                    )
                    if overlapping_bookings.exists():
                        form.add_error(
                            None,
                            "Hotel already booked for the selected dates")
                        messages.warning(
                            request,
                            "Hotel already booked for the selected dates")
                    else:
                        # Check additional validations
                        breakfast_included = form.cleaned_data.get(
                                                   'breakfast_included')
                        kids_club_tickets = form.cleaned_data.get('kids_club_tickets')
                        if breakfast_included and (
                           breakfast_included <
                           0 or breakfast_included > num_guests):
                            form.add_error(
                                'breakfast_included',
                                "Breakfast included cannot be greater than amount of guests."
                            )
                            messages.warning(
                                request,
                                "Breakfast included cannot be greater than amount of guests."
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
            # Handle form validation errors
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
    """
    This function handles the deletion of a booking identified by the
    provided booking_id. It retrieves the booking object associated with
    the provided ID and performs the deletion when a POST request is received.
    After successful deletion, it displays a success message and redirects
    the user to the booking overview page. Otherwise, it renders the
    'delete_booking.html' template, passing the booking object as context.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        # Perform booking deletion
        booking.delete()
        messages.success(request, "Booking deleted successfully.")
        return redirect('booking_overview')

    return render(request, 'delete_booking.html', {'booking': booking})


def custom_handler404(request, exception):
    """
    Custom handler for 404 (Page Not Found) errors.
    """
    return render(request, '404.html', status=404)

def custom_handler500(request):
    """
    Custom handler for 500 (Internal Server Error) errors.
    """
    return render(request, '500.html', status=500)
