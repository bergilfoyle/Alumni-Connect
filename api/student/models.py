from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    class Meta:
        db_table = 'students'
    usn = models.CharField(max_length=10, primary_key = True)
    sap_id = models.CharField(max_length=10, unique = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    personal_email = models.CharField(max_length=100, unique = True)
    email = models.CharField(max_length=100, unique = True)
    branch = models.CharField(max_length=50)
    year_joined = models.DateField()