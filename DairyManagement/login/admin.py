from django.contrib import admin

# Register your models here.
from .models import Worker,user

admin.site.register(Worker)
admin.site.register(user)