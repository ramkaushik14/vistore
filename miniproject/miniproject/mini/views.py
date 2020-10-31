from django.http import HttpResponse
from django.shortcuts import render
from .models import create, prod, orders


# Create your views here.
def home(request):
    dests = create.objects.all()
    return render(request, 'index.html', {"dests": dests})


def pro(request):
    dest1 = prod.objects.all()
    return render(request, 'index.html', {"dest1": dest1})


def orde(request):
    dest2 = orders.objects.all()
    return render(request, 'index.html', {"dest2": dest2})