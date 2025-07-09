# reservations/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Booking(models.Model):
    TABLE_CHOICES = [(i, f"Table {i}") for i in range(1, 21)]

    customer_name = models.CharField(max_length=100, verbose_name="Customer Name")
    email = models.EmailField(verbose_name="Email Address")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    date = models.DateField(verbose_name="Booking Date")
    time = models.TimeField(verbose_name="Booking Time")
    table_number = models.IntegerField(
        choices=TABLE_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(20)],
        verbose_name="Table Number"
    )
    number_of_guests = models.PositiveIntegerField(default=1, verbose_name="No. of Guests")
    special_requests = models.TextField(blank=True, verbose_name="Special Requests")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    class Meta:
        ordering = ['-date', 'time']
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        unique_together = ['date', 'time', 'table_number']

    def __str__(self):
        return f"{self.customer_name} - {self.date} {self.time} (Table {self.table_number})"
