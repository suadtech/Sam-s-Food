from django import forms
from .models import Reservation
from django.core.exceptions import ValidationError
import datetime

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer_name', 'customer_email', 'customer_phone', 
                 'reservation_date', 'reservation_time', 'party_size', 
                 'special_requests']
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date'}),
            'reservation_time': forms.TimeInput(attrs={'type': 'time'}),
            'special_requests': forms.Textarea(attrs={'rows': 3}),
        }
    
    def clean_reservation_date(self):
        date = self.cleaned_data['reservation_date']
        if date < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        return date
    
    def clean_party_size(self):
        party_size = self.cleaned_data['party_size']
        if party_size < 1:
            raise ValidationError("Party size must be at least 1")
        return party_size