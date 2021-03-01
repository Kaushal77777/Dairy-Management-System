from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class user(models.Model):
    user_fk=models.ForeignKey(User,on_delete=models.CASCADE)

class Worker(user):
   # worker_fk=models.ForeignKey(User,on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_dob = models.DateTimeField('date published')