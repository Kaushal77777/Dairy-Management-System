from django.shortcuts import render
from django.shortcuts import redirect
from .models import Destination
# Create your views here.


def index(request):

    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})


def payment(request):
    return render(request,"payment.html")


def paymentsuccessful(request):
    return render(request,"paymentsuccessful.html")