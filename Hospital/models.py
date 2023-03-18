from django.db import models
from django.contrib.auth.models import User

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
    user=models.OneToOneField(User,on_delete=models.CASCADE)
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
    d_image=models.ImageField(upload_to="photo/",null=True,blank=True)
    isApproved=models.BooleanField(default=False)
    spacility=models.CharField(max_length=120,choices=DISEASES)
    qualification=models.CharField(max_length=200)
    dateOfJoin=models.DateField(default=None,blank=True,null=True)
    salary = models.IntegerField(default=None,blank=True,null=True,)
    def __str__(self):
        return self.user.username
    
class Patient(models.Model):
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
    def __str__(self):
        return self.room_no
class CabilAuthorised(models.Model):
    cableNumber=models.ForeignKey("CABIL",on_delete=models.CASCADE,default=None,blank=True,null=True)
    doctor_no=models.ForeignKey("Doctor",on_delete=models.CASCADE,default=None,blank=True,null=True)
    isAvailable=models.BooleanField(default=True)
    def __str__(self):
        return self.cableNumber.CABIL_NUMBER

class MedicineModel(models.Model):
    patient=models.ForeignKey("Patient",on_delete=models.CASCADE,default=None,blank=True,null=True)
    pharmaceuticl=models.ForeignKey("Pharmaceuticl",on_delete=models.CASCADE,default=None,blank=True,null=True)
    doctor=models.ForeignKey("Doctor",on_delete=models.CASCADE,default=None,blank=True,null=True)
    action=models.BooleanField(default=True)
    def __str__(self):
        return self.patient
        
class Bill(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    payment_id=models.CharField(max_length=120)
    patient=models.ForeignKey("Patient",on_delete=models.CASCADE)
    doctor=models.ForeignKey("Doctor",on_delete=models.CASCADE)
    room=models.ForeignKey("Room",on_delete=models.CASCADE)
    pathology_fees=models.CharField(max_length=150)
    doctor_fees=models.CharField(max_length=150)
    tax=models.CharField(max_length=150)
    def __str__(self):
        return self.patient.first_name

class Payment(models.Model):
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE)
    month = models.CharField(max_length=200, choices=MONTHS)
    date_of_salary = models.DateField(auto_now=False, null=True,blank=True)
    status = models.BooleanField(default=False)
    amount = models.IntegerField(default=1000)

    def __str__(self):
        return self.doctor.user.username + " - " + self.month