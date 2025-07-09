from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'date', 'time', 'table_number', 'number_of_guests')
    list_filter = ('date', 'table_number')
    search_fields = ('customer_name', 'email', 'phone_number')
    ordering = ('-date', 'time')
