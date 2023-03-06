from django.shortcuts import render,redirect
from .form import * 
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as loginfunction , logout as logoutfunction

# ---------------------------------->>>HOME<<<-----------------------------------------#
def home(req):
    return render(req,"Patient/baseHome.html")
def about(req):
    return render(req,"Patient/about.html")
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
        if form.is_valid():
            form.save()
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
    return render(req,"Admin/Form/loginForm.html",{"form":LoginForm})
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
def viewPation(req,id):
    patient=Patient.objects.get(pk=id)
    return render(req,"Admin/Manage/Patient/SinglePatient.html",{"patient":patient})
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
    return render(req,"Admin/Manage/Room/manageRoom.html",data)
def editRoomDetails(req,id):
    roomDetail=Room.objects.get(pk=id)
    form=EditRoomForm(req.POST or None,instance=roomDetail)
    if req.method=="POST":
        if form.is_valid():
            form.save()
            return redirect(roomDetails)
    return render(req,"Admin/Edit/Room/room.html",{"form":form})
def cabilDetails(req):
    form = CabilForm(req.POST or None)
    data={}
    data['title']="Room Details"
    data['form']=form
    if req.method=="POST":
        if form.is_valid():
            form.save()
            return redirect(cabilDetails)
    data['cabinDetail']=CABIL.objects.all()
    return render(req,"Admin/Manage/Room/manageCabil.html",data)
def editCabilDetails(req,id):
    roomDetail=CABIL.objects.get(pk=id)
    form=EditCabilForm(req.POST or None,instance=roomDetail)
    if req.method=="POST":
        if form.is_valid():
            form.save()
            return redirect(cabilDetails)
    return render(req,"Admin/Edit/Room/cabil.html",{"form":form})