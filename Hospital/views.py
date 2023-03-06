from django.shortcuts import render,redirect
from .models import *
from .form import * 

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
def login(req):
    return render(req,"Patient/login.html")
def logout(req):
    pass
# ---------------------------------->>>DOCTOR<<<-----------------------------------------#
def newDoctor(req):
    form = DoctorForm(req.POST or None, req.FILES or None)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(home)
    return render(req,"Doctor/Form/doctorForm.html",{'form':form})
