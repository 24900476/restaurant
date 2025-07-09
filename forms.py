# reservations/forms.py
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'date': forms.SelectDateWidget(),
            'time': forms.TimeInput(format='%H:%M'),
            'special_requests': forms.Textarea(attrs={'rows': 3}),
        }
