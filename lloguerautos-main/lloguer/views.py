from django.shortcuts import render

# Create your views here.

from .models import Automobil

def automobil_list(request):
    automobiles = Automobil.objects.all()
    return render(request, 'automobil_list.html', {'automobiles': automobiles})
