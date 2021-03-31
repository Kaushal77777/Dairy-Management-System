from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("payment", views.payment, name="payment"),
    path("paymentsuccessful", views.paymentsuccessful, name="paymentsuccessful"),
    ]
