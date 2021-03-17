from django.urls import path
from viewdemoapp import views
urlpatterns = [
    path('', views.index,name='index'),
]