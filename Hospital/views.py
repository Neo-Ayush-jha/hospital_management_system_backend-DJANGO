from django.shortcuts import render,redirect
from .form import * 
from .models import *
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as loginfunction , logout as logoutfunction

# ---------------------------------->>>HOME<<<-----------------------------------------#
def home(req):
    return render(req,"Patient/baseHome.html")
def health(req):
    return render(req,"Patient/health.html")
# ---------------------------------->>>PATIENT<<<-----------------------------------------#
def newPatient(req):
    form = PatientForm(req.POST or None, req.FILES or None)
    if req.method =="POST":
        if form.is_valid():
            form.save()
            return redirect(home)
    return render(req,"Patient/Form/patientForm.html",{'form':form})
# ---------------------------------->>>DOCTOR<<<-----------------------------------------#
def newDoctor(req):
    form = DoctorForm(req.POST or None, req.FILES or None)
    if req.method == "POST":
        u = User()
        u.email=req.POST.get('email')
        u.username=req.POST.get('username')
        u.set_password(req.POST.get('password'))
        u.is_active =True
        u.is_staff=True
        u.save()

        a=Doctor()
        a.user=u
        a.father_name=req.POST.get('father_name')
        a.mother_name=req.POST.get('mother_name')
        a.age=req.POST.get('age')
        a.dob=req.POST.get('dob')
        a.blood_group=req.POST.get('blood_group')
        a.contact=req.POST.get('contact')
        a.city=req.POST.get('city')
        a.state=req.POST.get('state')
        a.gender=req.POST.get('gender')
        a.pin_code=req.POST.get('pin_code')
        a.nationality=req.POST.get('nationality')
        a.address=req.POST.get('address')
        a.d_image=req.FILES.get("d_image")
        a.spacility=req.POST.get('spacility')
        a.qualification=req.POST.get('qualification')
        a.qualification=req.POST.get('qualification')
        a.save()
        return redirect(home)
    return render(req,"Doctor/Form/doctorForm.html",{'form':form})
# ---------------------------------->>>ADMIN<<<-----------------------------------------#
@login_required
def adminHome(req):
    return render(req,"Admin/dashboard.html")
def login(req):
    LoginForm = AuthenticationForm(data=req.POST or None)
    if req.method =="POST":
        if LoginForm.is_valid():
            username = LoginForm.cleaned_data.get('username')
            password = LoginForm.cleaned_data.get("password")
            user = authenticate(username = username , password=password)
            if user is not None:
                print(user)
                loginfunction(req,user)
                return redirect(adminHome)
            else:
                return redirect(login)
    return render(req,"Patient/login.html",{"form":LoginForm})
@login_required
def logout(req):
    logoutfunction(req)
    return redirect(login)
def manageNewDoctor(req):
    data={}
    data['title']="New Appyly Doctor's"
    data['doctor']= Doctor.objects.filter(isApproved=False)
    return render(req,"Admin/Manage/Doctor/manageDoctor.html",data)
def manageOldDoctor(req):
    data={}
    data['title']="Old Doctor's"
    data['doctor']= Doctor.objects.filter(isApproved=True)
    return render(req,"Admin/Manage/Doctor/manageDoctor.html",data)
def viewDoctor(req,id):
    doctor=Doctor.objects.get(pk=id)
    return render(req,"Admin/Manage/Doctor/SingleDoctor.html",{"doctor":doctor})
def approveDoctor(req,id):
    doctor=Doctor.objects.get(id=id,isApproved=False)
    doctor.isApproved=True
    doctor.dateOfJoin=datetime.now()
    doctor.save()
    return redirect(manageOldDoctor)
def deleteDoctor(r,id):
    doctor=Doctor.objects.get(id=id)
    doctor.delete()
    return redirect(manageNewDoctor)
def editDoctor(req,id):
    doctor=Doctor.objects.get(pk=id)
    form=EditDoctorForm(req.POST or None,req.FILES or None,instance=doctor)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(manageOldDoctor)
    return render(req,"Admin/Edit/Doctor/doctor.html",{'form':form})
def managePation(req):
    data={}
    data['title']="Patient"
    data['patient']=Patient.objects.filter(isApproved=True)
    return render(req,"Admin/Manage/Patient/managePatient.html",data)
def manageOldPation(req):
    data={}
    data['title']="Patient old"
    data['patient']=Patient.objects.filter(isApproved=False)
    return render(req,"Admin/Manage/Patient/managePatient.html",data)
@login_required
def viewPation(req,id):
    patient=Patient.objects.get(pk=id)
    test=Test.objects.all()
    doctor=Doctor.objects.get(pk=req.user.id)
    form = ReportForm(req.POST or None,instance=doctor)
    if req.method=="POST":
        if form.is_valid():
            form=Report()
            form.test_name=req.POST.get('test_name')
            form.patient=patient
            form.doctor=doctor
            form.report=req.POST.get('report')
            form.test_price=req.POST.get('test_price')
            form.save()
            return redirect(managePation)
    report=Report.objects.all()
    return render(req,"Admin/Manage/Patient/SinglePatient.html",{"patient":patient,"form":form,"report":report,'test':test})
def editPation(req,id):
    patient=Patient.objects.get(pk=id)
    form=EditPatientForm(req.POST or None,req.FILES or None,instance=patient)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(managePation)
    return render(req,"Admin/Edit/Patient/patient.html",{'form':form})
def roomDetails(req):
    form = RoomForm(req.POST or None)
    data={}
    data['title']="Room Details"
    data['form']=form
    if req.method=="POST":
        if form.is_valid():
            form.save()
            return redirect(roomDetails)
    data['roomDetail']=Room.objects.all()
    return render(req,"Admin/Manage/Other/manageRoom.html",data)
def editRoomDetails(req,id):
    roomDetail=Room.objects.get(pk=id)
    form=EditRoomForm(req.POST or None,instance=roomDetail)
    if req.method=="POST":
        if form.is_valid():
            form.save()
            return redirect(roomDetails)
    return render(req,"Admin/Edit/Other/room.html",{"form":form})
def cabilDetails(req):
    form = CabilForm(req.POST or None)
    data={}
    data['title']="Cabil Details"
    data['form']=form
    if req.method=="POST":
        if form.is_valid():
            form.save()
            return redirect(cabilDetails)
    data['cabinDetail']=CABIL.objects.all()
    return render(req,"Admin/Manage/Other/manageCabil.html",data)
def editCabilDetails(req,id):
    roomDetail=CABIL.objects.get(pk=id)
    form=EditCabilForm(req.POST or None,instance=roomDetail)
    if req.method=="POST":
        if form.is_valid():
            form.save()
            return redirect(cabilDetails)
    return render(req,"Admin/Edit/Other/cabil.html",{"form":form})

def tests(req):
    form=TestForm(req.POST or None)
    data={}
    data['title']="All test's"
    data['form']=form
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(tests)
    data['test']=Test.objects.all()
    return render(req,"Admin/Manage/other/manageTest.html",data)

# def patientReport(req,id):
#     form = ReportForm(req.POST or None)
#     data={}
#     data['form']=form
#     data['test']=Test.objects.all()
#     data['patient']=Patient.objects.get(pk=id)
#     data['doctor']=Doctor.objects.get(user=req.user.id)
#     if req.method=="POST":
#         if form.is_valid():
#             form.save()
#         t=Report()
#         test=Test.objects.all()
#         patient=Patient.objects.get(pk=id)
#         doctor=Doctor.objects.get(user=req.user.id)
#         t.test_name=test
#         t.patient=patient
#         t.doctor=doctor
#         t.report=req.POST.get('report')
#         t.test_price=req.POST.get('test_price')
#         t.save()
#         return redirect(managePation)
#     return render(req,"Admin/Manage/Patient/SinglePatient.html",data)