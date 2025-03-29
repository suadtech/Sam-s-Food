from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Reservation, Table
from .forms import ReservationForm


# Create your views here.
def home(request):
    return render(request, 'bookings/home.html')

def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            messages.success(request, 'Your reservation has been created!')
            return redirect('bookings:reservation_manage', pk=reservation.id)
    else:
        form = ReservationForm()
    return render(request, 'bookings/reservation_form.html', {'form': form})

def reservation_manage(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'bookings/reservation_manage.html', {'reservation': reservation})

def reservation_cancel(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)   
   if request.method == 'POST':
        reservation.status = 'cancelled'
        reservation.save()
        messages.success(request, 'Your reservation has been cancelled.')
        return redirect('bookings:home')
    return render(request, 'bookings/reservation_cancel.html', {'reservation': reservation})
 

   