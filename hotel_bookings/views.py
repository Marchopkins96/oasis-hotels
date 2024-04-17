from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
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

def booking_create(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.hotel = hotel
            booking.user = request.user

            num_guests = form.cleaned_data['num_guests']
            if num_guests > hotel.max_guests:
                form.add_error('num_guests', "The number of guests entered exceeds the maximum allowed")  # noqa
                context = {'hotel': hotel, 'form': form}
                return render(request, 'my_booking.html', context)
            booking.save()
            messages.success(request, "New Booking created successfully")
            return redirect('booking_success', hotel_id=hotel.id, booking_id=booking.id)  # noqa
    else:
        form = BookingForm()

    context = {'hotel': hotel, 'form': form}
    return render(request, 'my_booking.html', context)

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
    return render(request, 'booking_success.html', {'bookings': bookings})

@login_required
def edit_booking(request, booking_id):

    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            num_guests = form.cleaned_data['num_guests']
            if num_guests > booking.hotel.max_guests:
                form.add_error('num_guests', "The number of guests entered exceeds the maximum allowed")  # noqa
                context = {'form': form, 'booking': booking}
                return render(request, 'edit_booking.html', context)

            form.save()
            messages.success(request, "Booking updated successfully")
            return redirect('booking_overview')
    else:
        form = BookingForm(instance=booking)
        context = {'form': form, 'booking': booking}

    return render(request, 'edit_booking.html', context)

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        booking.delete()
        return redirect('booking_overview')

    return redirect('booking_overview')
