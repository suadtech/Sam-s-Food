from django.shortcuts import render
from .models import MenuCategory
# Create your views here.
def menu_list(request):
    categories = MenuCategory.objects.prefetch_related('items').all()
    return render(request, 'menu/menu_list.html', {'categories': categories})