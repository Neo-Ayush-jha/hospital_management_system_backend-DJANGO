from django.forms import ModelForm
from .models import * 
class PatientForm(ModelForm):
    class Meta:
        model=Patient
        exclude=("isApproved","dateOfAdmission","dateOfDischarge","doctor","tests",)
class DoctorForm(ModelForm):
    class Meta:
        model=Doctor
        exclude=("isApproved","dateOfJoin","salary",)
class EditPatientForm(ModelForm):
    class Meta:
        model=Patient
        exclude=("isApproved",)
class EditDoctorForm(ModelForm):
    class Meta:
        model=Doctor
        fields="__all__"
class BillForm(ModelForm):
    class Meta:
        model=Bill
        fields="__all__"
class ReportForm(ModelForm):
    class Meta:
        model=Report
        exclude=("patient","doctor","report","action","report_image")
class EditReportForm(ModelForm):
    class Meta:
        model=Report
        exclude=("patient","doctor","test_name","action",)
class RoomForm(ModelForm):
    class Meta:
        model=Room
        exclude=("isAvailable",)
class EditRoomForm(ModelForm):
    class Meta:
        model=Room
        fields="__all__"
class CabilForm(ModelForm):
    class Meta:
        model=CABIL
        exclude=("isAvailable",)
class EditCabilForm(ModelForm):
    class Meta:
        model=CABIL
        fields="__all__"
class TestForm(ModelForm):
    class Meta:
        model=Test
        fields="__all__"
class RoomAuthorisedForm(ModelForm):
    class Meta:
        model = RoomAuthorised
        exclude=("isAvailable",)
class CabilAuthorisedForm(ModelForm):
    class Meta:
        model = CabilAuthorised
        exclude=("doctor_no",)
class PharmaceuticlForm(ModelForm):
    class Meta:
        model=Pharmaceuticl
        fields="__all__"
class MedicineModelForm(ModelForm):
    class Meta:
        model=MedicineModel
        exclude=("patient","doctor","action",)
class BillForm(ModelForm):
    class Meta:
        model=Bill
        fields="__all__"
class StaffForm(ModelForm):
    class Meta:
        model=Staff
        fields="__all__"
# class AttendanceForm(ModelForm):
#     class Meta:
#         model=Attendance
#         fields="__all__"
class NotificationForm(ModelForm):
    class Meta:
        model=Notification
        fields="__all__"
class Staff_leaveForm(ModelForm):
    class Meta:
        model=Staff_leave
        exclude=("status",)
class AppointmentForm(ModelForm):
    class Meta:
        model=Appointment
        exclude="__all__"


class Attendanceform(ModelForm):
    class Meta:
        model = Attendance
        fields = "__all__"