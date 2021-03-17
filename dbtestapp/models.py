from django.db import models

# Create your models here.
class Student(models.Model):
	student_name = models.CharField(max_length=100)
	student_dob = models.DateTimeField('date published')
class book_master(models.Model):
	book_id = models.IntegerField(primary_key=True)
	book_name = models.CharField(max_length=20)
	book_price = models.IntegerField()
