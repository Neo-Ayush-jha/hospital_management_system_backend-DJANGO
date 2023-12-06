from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
GENDER=(
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
# 22/032023
STAFF=(
    ("nurse","nurse"),
    ("receptionists","receptionists"),
    ("pherma_staff","pherma_staff"),
    ("pathology_staff","pathology_staff"),
    ("clerk","clerk"),
)
class Room(models.Model):
    room_no=models.CharField(max_length=12,choices=ROOM_NO)
    def __str__(self):
        return self.room_no    
class CABIL(models.Model):
    CABIL_NUMBER=models.CharField(max_length=12,choices=CABIL_NUMBER)
    def __str__(self):
        return self.CABIL_NUMBER    

class Test(models.Model):
    test_name=models.CharField(max_length=150,choices=TEST)
    test_price=models.IntegerField()
    def __str__(self):
        return self.test_name
    
    def __unicode__(self):
        return self.test_name

class Pharmaceuticl(models.Model):
    medicine=models.CharField(max_length=200,default=None,blank=True,null=True)
    price=models.FloatField()
    manufacturing_date=models.DateField()
    expiry_date=models.DateField()
    isbn_number=models.BigIntegerField(default=None,blank=True,null=True)
    isAvailable=models.BooleanField(default=False)
    def __str__(self):
        return self.medicine
     
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='doctor')
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    father_name=models.CharField(max_length=150)
    mother_name=models.CharField(max_length=150)
    age=models.IntegerField()
    gender=models.CharField(max_length=10,choices=GENDER)
    dob=models.DateField(help_text="use MM/DD/YYYY format")
    blood_group=models.CharField(max_length=10,choices=BLOOD)
    contact=models.IntegerField()
    city=models.CharField(max_length=150,choices=CITY)
    state=models.CharField(max_length=150,choices=(("Bihar","Bihar"),("Punjab","Punjab")))
    pin_code=models.IntegerField()
    nationality=models.CharField(max_length=150,choices=(("Indian","Indian"),("Other","Other")))
    d_image=models.ImageField(upload_to="photo/",null=True,blank=True)
    isApproved=models.BooleanField(default=False)
    spacility=models.CharField(max_length=120,choices=DISEASES)
    qualification=models.CharField(max_length=200)
    dateOfJoin=models.DateField(default=None,blank=True,null=True)
    salary = models.IntegerField(default=None,blank=True,null=True,)
    def __str__(self):
        return self.user.username
    def address(self):
        return self.city + ', ' + self.state + ', ' + self.nationality
    
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='student')
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    father_name=models.CharField(max_length=150)
    mother_name=models.CharField(max_length=150)
    age=models.IntegerField()
    gender=models.CharField(max_length=10,choices=GENDER)
    dob=models.DateField(help_text="use MM/DD/YYYY format")
    blood_group=models.CharField(max_length=10,choices=BLOOD)
    contact=models.IntegerField()
    city=models.CharField(max_length=150,choices=CITY)
    state=models.CharField(max_length=150,choices=(("Bihar","Bihar"),("Punjab","Punjab")))
    pin_code=models.IntegerField()
    nationality=models.CharField(max_length=150,choices=(("Indian","Indian"),("Other","Other")))
    address=models.TextField(default=None,blank=True,null=True,)
    p_image=models.ImageField(upload_to="photo/",null=True,blank=True)
    isApproved=models.BooleanField(default=True)
    problem=models.CharField(max_length=120,choices=DISEASES)
    dateOfAdmission=models.DateTimeField(auto_now_add=True)
    doctor=models.ForeignKey("Doctor",on_delete=models.CASCADE,default=None,blank=True,null=True)
    dateOfDischarge=models.DateField(help_text="use MM/DD/YYYY format",default=None,blank=True,null=True)
    tests=models.ForeignKey("Test",on_delete=models.CASCADE,default=None,blank=True,null=True)
    def __str__(self):
        return self.first_name + " - " + self.last_name
    def address(self):
        return self.city + ', ' + self.state + ', ' + self.nationality
        
class Report(models.Model):
    test_name=models.ForeignKey("Test",on_delete=models.CASCADE,default=None,blank=True,null=True)
    patient=models.ForeignKey("Patient",on_delete=models.CASCADE,default=None,blank=True,null=True)
    doctor=models.ForeignKey("Doctor",on_delete=models.CASCADE,default=None,blank=True,null=True)
    report=models.TextField(default=None,blank=True,null=True)
    report_image=models.ImageField(upload_to="report/",null=True,blank=True)
    action=models.BooleanField(default=None,blank=True,null=True)
    # def __str__(self):
    #     return self.patient

class RoomAuthorised(models.Model):
    room_no=models.ForeignKey("Room",on_delete=models.CASCADE,default=None,blank=True,null=True)
    patient_no=models.ForeignKey("Patient",on_delete=models.CASCADE,default=None,blank=True,null=True)
    isAvailable=models.BooleanField(default=True)
    room_fee=models.IntegerField(default=500)

    def __str__(self):
        return self.room_no
    
class CabilAuthorised(models.Model):
    cableNumber=models.OneToOneField("CABIL",on_delete=models.CASCADE,default=None,blank=True,null=True)
    doctor_no=models.ForeignKey("Doctor",on_delete=models.CASCADE,default=None,blank=True,null=True)
    isAvailable=models.BooleanField(default=True)
    def __str__(self):
        return self.cableNumber.CABIL_NUMBER

# 22/032023
class Staff(models.Model):
    staff_name=models.CharField(max_length=150)
    staff_post=models.CharField(max_length=20,choices=STAFF)
    rf_code= models.CharField(max_length=100,default=None,blank=True,null=True,unique=True)
    staff_payment=models.IntegerField(default=1000)
    def __str__(self):
        return self.staff_name
    
class MedicineModel(models.Model):
    patient=models.ForeignKey("Patient",on_delete=models.CASCADE,default=None,blank=True,null=True)
    pharmaceuticl=models.ForeignKey("Pharmaceuticl",on_delete=models.CASCADE,default=None,blank=True,null=True)
    doctor=models.ForeignKey("Doctor",on_delete=models.CASCADE,default=None,blank=True,null=True)
    action=models.BooleanField(default=True)
    # 22/032023
    qty = models.IntegerField(default=1)
    def __str__(self):
        return self.patient.first_name +"-"+ self.patient.last_name +"  -   "+self.pharmaceuticl.medicine
    def get_price(self):
        return self.pharmaceuticl.price*self.qty
    
class Bill(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,default=None,blank=True,null=True)
    staff=models.ForeignKey(Staff,on_delete=models.CASCADE)
    room=models.ForeignKey(RoomAuthorised,on_delete=models.CASCADE,default=None,blank=True,null=True)
    madicine=models.ManyToManyField(MedicineModel)
    report=models.ManyToManyField(Report,default=None,blank=True,null=True)
    doctor_fee=models.IntegerField(default=1000)
    # def __str__(self):
    #     return self.patient.first_name
    
    def extra_price(self):
        total=0
        for bi in self.madicine.all():
            total += bi.get_price()
        if self.report:
            for re in self.report.all():
                total+=re.test_name.test_price
        return total
    
    def total_price(self):
        total=0
        total+=self.extra_price()
        if self.room:
            total+=self.room.room_fee
        total+=self.doctor_fee
        total*0.18
        return total
    
class Payment(models.Model):
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE)
    month = models.CharField(max_length=200, choices=MONTHS)
    date_of_salary = models.DateField(auto_now=False, null=True,blank=True)
    status = models.BooleanField(default=False)
    amount = models.IntegerField(default=1000)
    def __str__(self):
        return self.doctor.user.username + " - " + self.month

class Notification(models.Model):
    staff_id = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    message=models.TextField()
    created_as=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.staff_id.user.username

class Staff_leave(models.Model):
    staff_id = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date=models.CharField(max_length=150)
    message=models.TextField()
    status=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.staff_id.user.username

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(help_text="use MM-DD-YYYY format")
    start=models.TimeField()
    end=models.TimeField()
    def __str__(self):
        return self.patient.first_name + " - " + self.patient.last_name + " - " + self.doctor.user.username
    
class Attendance(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=False, blank=False)
    end_time = models.DateTimeField(default=False, blank=False)
    Date = models.DateTimeField(auto_now_add=True)
    is_present = models.BooleanField(default=False, blank=False)
    def __str__(self):
        return self.Doctor.user.username