from dataclasses import fields
from rest_framework import serializers
from .models import Aadhar, Address, PastJobExperience, PersonalDetail, BankDetail, Qualification

class AadharSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aadhar
        fields = '__all__'

class PersonalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetail
        fields = ['full_name', 'dob', 'blood_group', 'contact_number', 'email']      
        
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'city', 'state', 'postal_code']
        
class BankDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetail
        fields = ['acc_number', 'bank_name', 'ifsc_code']
        
class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ['college_name', 'yop', 'percentage']
            
class PastJobExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastJobExperience
        fields = ['company_name', 'job_role', 'experience_in_years']