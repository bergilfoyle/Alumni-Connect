from django.db import models
from django.contrib.auth.models import User

class Alumni(models.Model):
    usn = models.CharField(max_length=10, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='alumnus_details')
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=10, null=True)
    personal_email = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    branch = models.CharField(max_length=50, null=True)
    year_joined = models.DateField(null = True)
    year_passed = models.DateField(null = True)

    class Meta:
        db_table = 'alumni'


class Internships(models.Model):
    alumnus = models.OneToOneField(Alumni, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, null=True)
    stipend = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'internships'


class Placements(models.Model):
    alumnus = models.OneToOneField(Alumni, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    job_profile = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, null=True)
    ctc = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'placements'


class HigherStudies(models.Model):
    alumnus = models.OneToOneField(Alumni, on_delete=models.CASCADE)
    college_name = models.CharField(max_length=50)
    degree = models.CharField(max_length=10, null=True)
    start_year = models.DateField(null= True)
    end_year = models.DateField(null = True)

    class Meta:
        db_table = 'higher_studies'