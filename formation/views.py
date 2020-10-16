from django.shortcuts import render
from .models import Offres

def formation_index(request):
    offres = Offres.objects.all()
    return render(request,'offres.html', {'offres':offres} )