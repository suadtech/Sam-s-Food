from django.contrib import admin
from .models import Table, Reservation
# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity', 'location')
    search_fields = ('table_number', 'location')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'reservation_date', 'reservation_time', 'party_size', 'status')
    list_filter = ('status', 'reservation_date')
    search_fields = ('customer_name', 'customer_email')
    filter_horizontal = ('tables',)