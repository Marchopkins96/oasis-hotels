from django.contrib import admin
from .models import Hotel, Booking, Extras

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    """
    This class defines the custom admin interface for the Booking model.

    It specifies the list of fields to be displayed in the admin list
    view for Booking objects.
    """
    list_display = ['id',
                    'user',
                    'hotel',
                    'check_in_date',
                    'check_out_date',
                    'breakfast_included',
                    'kids_club_tickets']


# Registering the models in the admin site
admin.site.register(Extras)
admin.site.register(Hotel)
admin.site.register(Booking, BookingAdmin)