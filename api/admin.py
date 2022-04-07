from django.contrib import admin
from .models import Aadhar, Address, PersonalDetail, PastJobExperience, BankDetail, Qualification

# Register your models here.
class AadharAdmin(admin.ModelAdmin):
    list_display = ('aadhar_number', 'is_active')
   
admin.site.register(Aadhar, AadharAdmin)  

class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'state', 'postal_code')
   
admin.site.register(Address, AddressAdmin) 

class PersonalDetailAdmin(admin.ModelAdmin):
    list_display = ('aadhar_number', 'full_name', 'dob', 'blood_group', 'contact_number', 'email')
   
admin.site.register(PersonalDetail, PersonalDetailAdmin)

class BankDetailAdmin(admin.ModelAdmin):
    list_display = ('acc_number', 'bank_name', 'ifsc_code')
   
admin.site.register(BankDetail, BankDetailAdmin)

class QualificationAdmin(admin.ModelAdmin):
    list_display = ('college_name', 'yop', 'percentage')
   
admin.site.register(Qualification, QualificationAdmin)

class PastJobExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'job_role', 'experience_in_years')
   
admin.site.register(PastJobExperience, PastJobExperienceAdmin)


# admin.site.register(Aadhar)
# admin.site.register(Address)
# admin.site.register(PersonalDetail)
# admin.site.register(BankDetail)
# admin.site.register(PastJobExperience)
# admin.site.register(Qualification)