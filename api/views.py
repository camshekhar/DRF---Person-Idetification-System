from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Aadhar, Address, BankDetail, PastJobExperience, PersonalDetail, Qualification
from .serializers import PersonalDetailSerializer, AadharSerializer, AddressSerializer, BankDetailSerializer, QualificationSerializer, PastJobExperienceSerializer

# RETRIEVE Requests Starts Here........
@api_view(['GET'])
def getAadharDetails(request):
    adhar = Aadhar.objects.all()
    data = AadharSerializer(adhar, many=True).data
    return Response(data)

@api_view(['GET'])
def getAdharPersonalDetails(request):
    personalDetail = PersonalDetail.objects.all()
    data = PersonalDetailSerializer(personalDetail, many=True).data 
    return Response(data)

@api_view(['GET'])
def getAdharAddress(request):
    addressDetail = Address.objects.all()
    data = AddressSerializer(addressDetail, many=True).data
    return Response(data)

@api_view(['GET'])
def getAdharBankDetails(request):
    addressDetail = BankDetail.objects.all()
    data = BankDetailSerializer(addressDetail, many=True).data
    return Response(data)

@api_view(['GET'])
def getQualificationDetails(request):
    addressDetail = Qualification.objects.all()
    data = QualificationSerializer(addressDetail, many=True).data
    return Response(data)

@api_view(['GET'])
def getPastJobExpDetails(request):
    expDetails = PastJobExperience.objects.all()
    serializer = PastJobExperienceSerializer(expDetails, many=True)
    return Response(serializer.data)


#  CREATE Requests Starts Here.......
@api_view(['POST'])
def addAadhar(request):
    serializer = AadharSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def addAdharPersonalDetails(request):
    serializer = PersonalDetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def addAdharAddress(request):
    serializer = AddressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
@api_view(['POST'])
def addAdharBankDetails(request):
    serializer = BankDetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addQualificationDetails(request):
    serializer = QualificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addPastJobExpDetails(request):
    serializer = PastJobExperienceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# UPDATE requests Starts Here....
@api_view(['POST'])
def updateAdharPersonalDetails(request, pk):
    personDetails = PersonalDetail.objects.get(pk=pk)
    serializer = PersonalDetailSerializer(instance= personDetails, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def updateAdharAddress(request, pk):
    address = Address.objects.get(pk=pk)
    serializer = AddressSerializer(instance= address, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def updateAdharBankDetails(request, pk):
    bankDetails = BankDetail.objects.get(pk=pk)
    serializer = BankDetailSerializer(instance= bankDetails, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def updateAdharStatus(request, pk):
    aadharDetails = Aadhar.objects.get(pk=pk)
    serializer = AadharSerializer(instance= aadharDetails, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def updateQualificationDetails(request, pk):
    qualificationDetails = Qualification.objects.get(pk=pk)
    serializer = QualificationSerializer(instance= qualificationDetails, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def updatePastJobExpDetails(request, pk):
    expDetails = PastJobExperience.objects.get(pk=pk)
    serializer = PastJobExperienceSerializer(instance= expDetails, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE Request Handled Here....
@api_view(['DELETE'])
def deleteAadhar(request, pk):
    aadhar = Aadhar.objects.get(pk=pk)
    aadhar.delete()
    pd = PersonalDetail.objects.get(pk=pk)
    pd.delete()
    add = Address.objects.get(pk=pk)
    add.delete()
    bank = BankDetail.objects.get(pk=pk)
    bank.delete()
    qualf = Qualification.objects.get(pk=pk)
    qualf.delete()
    exp = PastJobExperience.objects.get(pk=pk)
    exp.delete()
    return Response("Item Successfully Deleted!")


    