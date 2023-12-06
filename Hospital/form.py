from django.forms import ModelForm
from .models import * 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.db import transaction
from django.contrib.auth.hashers import make_password

User = get_user_model()
GENDER_CHOICES=(
    ("Mail","Mail"),
    ("Femail","Femail"),
    ("Other","Other")
)
BLOOD=(
    ("O+","O+"),
    ("O-","O-"),
    ("A+","A+"),
    ("A-","A-"),
    ("B+","B+"),
    ("B-","B-"),
    ("AB+","AB+"),
    ("AB-","AB-"),
)
ROOM_NO=(
    ("101","101"),
    ("102","102"),
    ("103","103"),
    ("104","104"),
    ("105","105"),
    ("106","106"),
    ("107","107"),
    ("108","108"),
    ("109","109"),
    ("110","110"),
    ("111","111"),
    ("112","112"),
    ("113","113"),
    ("114","114"),
    ("115","115"),
    ("116","116"),
    ("117","117"),
    ("118","118"),
    ("119","119"),
    ("120","120"),
)
MONTHS = (
    ("jan","january"),
    ("feb","feb"),
    ("march","march"),
    ("april","april"),
    ("may","may"),
    ("june","june"),
    ("july","july"),
    ("aug","aug"),
    ("sep","sep"),
    ("oct","oct"),
    ("nov","nov"),
    ("dec","dec"),
)
CABIL_NUMBER=(
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
    ("6","6"),
    ("7","7"),
    ("8","8"),
    ("9","9"),
    ("10","10"),
    ("11","11"),
    ("12","12"),
    ("13","13"),
    ("14","14"),
    ("15","15"),
    ("16","16"),
    ("17","17"),
    ("18","18"),
    ("19","19"),
    ("20","20"),
)
DISEASES=(
    ("Heart disease","Heart disease"),
    ("Liver disease","Liver disease"),
    ("Kidney disease","Kidney disease"),
    ("Brain disease","Brain disease"),
    ("Neurological problem","Neurological problem"),
    ("Acidity","Acidity"),
    ("Appendicitis","Appendicitis"),
    ("Dyspepsia","Dyspepsia"),
    ("Food poisoning","Food poisoning"),
    ("Food Gastritis","Food Gastritis"),
    ("Food IBS","Food IBS"),
    ("Peptic ulcer","Peptic ulcer"),
    ("Food allergy","Food allergy"),
    ("Respiratory disease","Respiratory disease"),
    ("Eye conditions","Eye conditions"),
    ("Endocrin diseases","Endocrin diseases"),
    ("Nerve disorders","Nerve disorders"),
    ("Blood diseases","Blood diseases"),
    ("Bone or joint diseases","Bone or joint diseases"),
    ("Skin diseases","Skin diseases"),
    ("Cancer","Cancer"),
    ("Autoimmune diseases","Autoimmune diseases"),
    ("Other diseases","Other diseases"),
)
CITY = (
    ("Purnea", "Purnea"),
    ("Patna", "Patna"),
    ("Bhagalpur", "Bhagalpur"),
    ("Bhopal", "Bhopal"),
    ("indore", "indore"),
    ("Delhi", "Delhi"),
    ("Kolkata", "Kolkata"),
    ("Pune", "Pune"),
    ("Goa", "Goa"),
    ("Jalandher", "Jalandher"),
    ("Dharbhanga", "Dharbhanga"),
    ("Rachi", "Rachi"),
)
TEST=(
    ("blood count","blood count"),
    ("blood typing","blood typing"),
    ("glucose tolerance test","glucose tolerance test"),
    ("thymol turbidity","thymol turbidity"),
    ("liver function test","liver function test"),
    ("kidney function test","kidney function test"),
    ("lumbar puncture","lumbar puncture"),
    ("toxicology test","toxicology test"),
    ("angiocardiography","angiocardiography"),
    ("cholecystography","cholecystography"),
    ("ECG","ECG"),
    ("X-ray","X-ray"),
)
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class PatientForm(ModelForm):
    email=forms.EmailField(widget=forms.EmailInput())
    set_password=forms.CharField(widget=forms.PasswordInput())
    username=forms.CharField(widget=forms.TextInput())
    first_name=forms.CharField(widget=forms.TextInput())
    last_name=forms.CharField(widget=forms.TextInput())
    father_name=forms.CharField(widget=forms.TextInput())
    mother_name=forms.CharField(widget=forms.TextInput())
    dob=forms.DateField(widget=forms.DateInput())
    age=forms.IntegerField(widget=forms.NumberInput())
    gender= forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect())
    blood_group= forms.ChoiceField(choices=BLOOD,widget=forms.RadioSelect())
    contact = forms.IntegerField(widget=forms.NumberInput())
    city= forms.ChoiceField(choices=CITY,widget=forms.RadioSelect())
    state=forms.ChoiceField(choices=(("Bihar","Bihar"),("Punjab","Punjab")), widget=forms.RadioSelect())
    nationality=forms.ChoiceField(choices=(("Indian","Indian"),("Other","Other")), widget=forms.RadioSelect())
    pin_code = forms.IntegerField(widget=forms.NumberInput())
    p_image=forms.ImageField(widget=forms.FileInput())
    problem = forms.ChoiceField(choices=DISEASES, widget=forms.RadioSelect())

    class Meta:
        model=User
        fields = ('username','email','password')
    @transaction.atomic
    def save(self,commit=True):
        user = super().save(commit=False)
        user.is_patient=True
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        patient = Patient.objects.create(
            user = user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            father_name=self.cleaned_data['father_name'],
            mother_name=self.cleaned_data['mother_name'],
            age= self.cleaned_data['age'],
            gender=self.cleaned_data['gender'],
            dob=self.cleaned_data['dob'],
            blood_group=self.cleaned_data['blood_group'],
            city=self.cleaned_data['city'],
            state=self.cleaned_data['state'],
            nationality=self.cleaned_data['nationality'],
            pin_code=self.cleaned_data['pin_code'],
            p_image=self.cleaned_data['p_image'],
            problem=self.cleaned_data['problem'],
            contact=self.cleaned_data['contact']
        )
        return user
class DoctorForm(ModelForm):
    email=forms.EmailField(widget=forms.EmailInput())
    set_password = forms.CharField(widget=forms.PasswordInput)
    # password2 = forms.CharField(widget=forms.PasswordInput())
    username=forms.CharField(widget=forms.TextInput())
    first_name=forms.CharField(widget=forms.TextInput())
    last_name=forms.CharField(widget=forms.TextInput())
    father_name=forms.CharField(widget=forms.TextInput())
    mother_name=forms.CharField(widget=forms.TextInput())
    age=forms.IntegerField(widget=forms.NumberInput())
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    dob=forms.DateField(widget=forms.DateInput())
    contact=forms.IntegerField(widget=forms.NumberInput())
    blood_group=forms.ChoiceField(choices=BLOOD, widget=forms.RadioSelect())
    city=forms.ChoiceField(choices=CITY, widget=forms.RadioSelect())
    state=forms.ChoiceField(choices=(("Bihar","Bihar"),("Punjab","Punjab")), widget=forms.RadioSelect())
    pin_code=forms.IntegerField(widget=forms.NumberInput())
    nationality=forms.ChoiceField(choices=(("Indian","Indian"),("Other","Other")), widget=forms.RadioSelect())
    d_image=forms.ImageField(widget=forms.FileInput())
    spacility=forms.ChoiceField(choices=DISEASES, widget=forms.RadioSelect())
    qualification=forms.CharField(widget=forms.TextInput())
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        user.set_password(self.cleaned_data['password'])
        
        if commit:
            user.save()
        
        doctor = Doctor.objects.create(
            user=user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            father_name=self.cleaned_data['father_name'],
            mother_name=self.cleaned_data['mother_name'],
            age=self.cleaned_data['age'],
            gender=self.cleaned_data['gender'],
            dob=self.cleaned_data['dob'],
            blood_group=self.cleaned_data['blood_group'],
            city=self.cleaned_data['city'],
            state=self.cleaned_data['state'],
            pin_code=self.cleaned_data['pin_code'],
            nationality=self.cleaned_data['nationality'],
            d_image=self.cleaned_data['d_image'],
            spacility=self.cleaned_data['spacility'],
            qualification=self.cleaned_data['qualification'],
            contact=self.cleaned_data['contact']
        )
        return user
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
        fields=['date','start']


class Attendanceform(ModelForm):
    class Meta:
        model = Attendance
        fields = "__all__"