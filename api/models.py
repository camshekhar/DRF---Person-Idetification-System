from django.db import models

# Create your models here.

class Aadhar(models.Model):
    aadhar_number = models.CharField(max_length=25, primary_key=True)
    is_active = models.BooleanField(default=False)  
    
     
class Address(models.Model):
    aadhar_number = models.CharField(max_length=25, primary_key=True)
    street = models.CharField(max_length= 100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20, null=True)
    
    
class Qualification(models.Model):
    aadhar_number = models.CharField(max_length=25, primary_key=True)
    college_name = models.CharField(max_length=100, null=True)
    yop = models.CharField(max_length=25, null=True)
    percentage = models.CharField(max_length=10, null=True)
    
    
class BankDetail(models.Model):
    aadhar_number = models.CharField(max_length=25, primary_key=True)
    acc_number = models.CharField(max_length=50, null=True)
    bank_name = models.CharField(max_length=50, null=True)
    ifsc_code = models.CharField(max_length=20, null=True)
    
class PastJobExperience(models.Model):
    aadhar_number = models.CharField(max_length=25, primary_key=True)
    company_name = models.CharField(max_length=50, null=True)
    job_role = models.CharField(max_length=50, null=True)
    experience_in_years = models.CharField(max_length=50, null=True)
         
class PersonalDetail(models.Model):
    aadhar_number = models.CharField(max_length=25, primary_key=True)
    full_name = models.CharField(max_length=100, null=True)
    dob = models.CharField(max_length=50, null=True)
    blood_group = models.CharField(max_length=10, null=True)
    contact_number = models.CharField(max_length=12, null=True)
    email = models.CharField(max_length=50, null=True)
    
    


    