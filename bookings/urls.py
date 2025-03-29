from django.urls import path
from . import views

app_name = 'bookings'
urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.reservation_create, name='reservation_create'),
    path('manage/<int:pk>/', views.reservation_manage, name='reservation_manage'),
]