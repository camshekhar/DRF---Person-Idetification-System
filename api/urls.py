from django.urls import path, include
from . import views


urlpatterns = [
    # URLs for RETRIEVE data.
    path('AadharDetails/<str:pk>/', views.getAadharDetails),
    # path('Aadhar/PersonalDetail/', views.getAdharPersonalDetails),
    # path('Aadhar/Address/', views.getAdharAddress),
    # path('Aadhar/Qualification/', views.getQualificationDetails),
    # path('Aadhar/Bank/', views.getAdharBankDetails),
    # path('Aadhar/PastJobExp/', views.getPastJobExpDetails),
    
    # URLs for CREATE data.
    path('Aadhar/addNewAadhar', views.addAadhar),
    path('Aadhar/PersonalDetail/addPersonalDetail', views.addAdharPersonalDetails),
    path('Aadhar/Address/addAddress', views.addAdharAddress),
    path('Aadhar/Bank/addBankDetails', views.addAdharBankDetails),
    path('Aadhar/Qualification/addQualificationDetails', views.addQualificationDetails),
    path('Aadhar/PastJobExperience/addPastJobExpDetails', views.addPastJobExpDetails),
    
    # URLs for UPDATE data.
    path('Aadhar/updateAdharStatus/<str:pk>', views.updateAdharStatus),
    path('Aadhar/PersonalDetail/updatePersonalDetail/<str:pk>', views.updateAdharPersonalDetails),
    path('Aadhar/Address/updateAddress/<str:pk>', views.updateAdharAddress),
    path('Aadhar/Bank/updateAdharBankDetails/<str:pk>', views.updateAdharBankDetails),
    path('Aadhar/Qualification/updateQualificationDetails/<str:pk>', views.updateQualificationDetails),
    path('Aadhar/PastJobExp/updatePastJobExpDetails/<str:pk>', views.updatePastJobExpDetails),
    
    # URLs for DELETE data.
    path('Aadhar/DeleteAadhar/<str:pk>/', views.deleteAadhar),
    

]

