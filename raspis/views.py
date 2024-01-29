from django.shortcuts import render
from .models import Shed

def raspis_home(request):
    raspis = Shed.objects.all()
    return render(request, 'raspis/raspis_home.html', {'raspis': raspis})
