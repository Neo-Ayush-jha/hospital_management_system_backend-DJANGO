from django.forms import ModelForm
from .models import * 
class PatientForm(ModelForm):
    class Meta:
        model=Patient
        exclude=("room_no","isApproved","dateOfAdmission","dateOfDischarge")
class DoctorForm(ModelForm):
    class Meta:
        model=Doctor
        exclude=("cableNumber","isApproved","dateOfJoin","salary","spacility")
class EditPatientForm(ModelForm):
    class Meta:
        model=Patient
        exclude=("isApproved",)
class EditDoctorForm(ModelForm):
    class Meta:
        model=Doctor
        exclude=("isApproved",)
class BillForm(ModelForm):
    class Meta:
        model=Bill
        fields="__all__"
class ReportForm(ModelForm):
    class Meta:
        model=Report
        fields="__all__"
class RoomForm(ModelForm):
    class Meta:
        model=Room
        fields="__all__"