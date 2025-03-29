from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Table(models.Model):
    table_number = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField(default=2)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Table {self.table_number} ({self.capacity} seats)"

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]  

    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    party_size = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)]
    )

    statuspecial_requests = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')
    tables = models.ManyToManyField(Table)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Reservation #{self.id} - {self.customer_name}"   