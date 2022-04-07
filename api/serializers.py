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
        fields = '__all__'       
        
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        
class BankDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetail
        fields = '__all__'
        
class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'
            
class PastJobExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastJobExperience
        fields = '__all__'