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
    data={}
    data['patient']=Patient.objects.all().count()
    data['doctor']=Doctor.objects.filter(isApproved=True).count()
    data['newDoctor']=Doctor.objects.filter(isApproved=False).count()
    data['totalTest']=Report.objects.filter(action=True).count()
    data['test']=Report.objects.filter(action=None).count()
    data['room']=Room.objects.all().count()
    data['notRoomAvailable']=RoomAuthorised.objects.filter(isAvailable=False).count()
    data['cabil']=CABIL.objects.all().count()
    data['notCabilAvailable']=CabilAuthorised.objects.filter(isAvailable=False).count()
    return render(req,"Admin/dashboard.html",data)

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


@login_required
def manageNewDoctor(req):
    data={}
    data['title']="New Appyly Doctor's"
    data['doctor']= Doctor.objects.filter(isApproved=False)
    return render(req,"Admin/Manage/Doctor/manageDoctor.html",data)
@login_required
def manageOldDoctor(req):
    data={}
    data['title']="Old Doctor's"
    data['doctor']= Doctor.objects.filter(isApproved=True)
    return render(req,"Admin/Manage/Doctor/manageDoctor.html",data)
@login_required
def viewDoctor(req,id):
    doctor=Doctor.objects.get(pk=id)
    form=CabilAuthorisedForm(req.POST or None)
    cabil=CABIL.objects.all()
    if req.method =="POST":
        if form.is_valid():
            cabilNumber=req.POST.get("cabilNumber")
            form=CabilAuthorised()
            form.doctor_no=doctor
            form.cableNumber=CABIL.objects.get(pk=cabilNumber)
            form.isAvailable=False
            form.save()
            return redirect(viewDoctor,id)
    
    cabilAprove=CabilAuthorised.objects.get(doctor_no=doctor.id)
    # cabilAprove=CabilAuthorised.objects.all()
    return render(req,"Admin/Manage/Doctor/SingleDoctor.html",{"doctor":doctor,"form":form,"cabil":cabil,"cabilAprove":cabilAprove})
@login_required
def approveDoctor(req,id):
    doctor=Doctor.objects.get(id=id,isApproved=False)
    doctor.isApproved=True
    doctor.dateOfJoin=datetime.now()
    doctor.save()
    return redirect(approveDoctor,id)
@login_required
def deleteDoctor(r,id):
    doctor=Doctor.objects.get(id=id)
    doctor.delete()
    return redirect(manageNewDoctor)
@login_required
def editDoctor(req,id):
    doctor=Doctor.objects.get(pk=id)
    form=EditDoctorForm(req.POST or None,req.FILES or None,instance=doctor)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(manageOldDoctor)
    return render(req,"Admin/Edit/Doctor/doctor.html",{'form':form})


@login_required
def managePation(req):
    data={}
    data['title']="Patient"
    data['patient']=Patient.objects.filter(isApproved=True)
    return render(req,"Admin/Manage/Patient/managePatient.html",data)
@login_required
def manageOldPation(req):
    data={}
    data['title']="Patient old"
    data['patient']=Patient.objects.filter(isApproved=False)
    return render(req,"Admin/Manage/Patient/managePatient.html",data)
@login_required
def viewPation(req,id):
    patient=Patient.objects.get(pk=id)
    test=Test.objects.all()
    doctor=Doctor.objects.get(user=req.user.id)
    form = ReportForm(req.POST or None,instance=doctor)
    if req.method=="POST":
        print(req.POST.get('test_name'))
        if form.is_valid():
            test_name = req.POST.get('test_name')
            form=Report()
            form.test_name= Test.objects.get(pk=test_name)
            form.patient=patient
            form.doctor=doctor
            # form.report=req.POST.get('report')
            form.save()
            return redirect(viewPation,id)
    report=Report.objects.all()
    return render(req,"Admin/Manage/Patient/SinglePatient.html",{"patient":patient,"form":form,"report":report,'test':test})
@login_required
def viewReport(req,id):
    report=Report.objects.get(pk=id)
    form = EditReportForm(req.POST or None,req.FILES or None,instance=report)
    if req.method=="POST":
        if form.is_valid():
            form=report
            form.action=True
            form.save()
            return redirect(viewReport,id)
    return render(req,"Admin/Manage/Patient/report.html",{"form":form,"report":report})
@login_required
def editPation(req,id):
    patient=Patient.objects.get(pk=id)
    form=EditPatientForm(req.POST or None,req.FILES or None,instance=patient)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(managePation)
    return render(req,"Admin/Edit/Patient/patient.html",{'form':form})

    
@login_required
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
    data['roomA']=RoomAuthorised.objects.all()
    return render(req,"Admin/Manage/Other/manageRoom.html",data)
@login_required
def editRoomDetails(req,id):
    roomDetail=Room.objects.get(pk=id)
    form=EditRoomForm(req.POST or None,instance=roomDetail)
    if req.method=="POST":
        if form.is_valid():
            form.save()
            return redirect(roomDetails)
    return render(req,"Admin/Edit/Other/room.html",{"form":form})

    
@login_required
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
@login_required
def editCabilDetails(req,id):
    roomDetail=CABIL.objects.get(pk=id)
    form=EditCabilForm(req.POST or None,instance=roomDetail)
    if req.method=="POST":
        if form.is_valid():
            form.save()
            return redirect(cabilDetails)
    return render(req,"Admin/Edit/Other/cabil.html",{"form":form})

    
@login_required
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
    data['report']=Report.objects.all()
    return render(req,"Admin/Manage/other/manageTest.html",data)




@login_required
def doctorDashboard(req):   
    data={}
    data['doctor']=Doctor.objects.get(pk=req.user.id)
    data['patient']=Patient.objects.all().count()
    data['room']=Room.objects.all().count()
    data['notRoomAvailable']=RoomAuthorised.objects.filter(isAvailable=False).count()
    data['cabil']=CABIL.objects.all().count()
    data['notCabilAvailable']=CabilAuthorised.objects.filter(isAvailable=False).count()
    return render(req,"Doctor/dashboard.html",data)
@login_required
def managePationD(req):
    data={}
    data['title']="Patient"
    doctor=Doctor.objects.get(id=req.user.id)
    data['doctor']=Doctor.objects.get(pk=req.user.id)
    data['patient']=Patient.objects.filter(isApproved=True , doctor = doctor)
    return render(req,"Doctor/Manage/managePatient.html",data)
@login_required
def manageOldPationD(req):
    data={}
    data['doctor']=Doctor.objects.get(pk=req.user.id)
    data['title']="Patient old"
    data['patient']=Patient.objects.filter(isApproved=False)
    return render(req,"Doctor/Manage/managePatient.html",data)
@login_required
def viewPationD(req,id):
    patient=Patient.objects.get(pk=id)
    test=Test.objects.all()
    doctor=Doctor.objects.get(pk=req.user.id)
    pharmaceuticl=Pharmaceuticl.objects.all()
    form = ReportForm(req.POST or None,instance=doctor)
    formMedicin=MedicineModelForm(req.POST or None,instance=doctor)
    if req.method=="POST":
        if form.is_valid():
            test_name = req.POST.get('test_name')
            form=Report()
            form.test_name= Test.objects.get(pk=test_name)
            form.patient=patient
            form.doctor=doctor
            # form.report=req.POST.get('report')
            form.save()
            return redirect(viewPationD,id)
    if req.method=="POST":
        if formMedicin.is_valid():
            pharmaceuticl=req.POST.get('pharmaceuticl')
            formMedicin=MedicineModel()
            formMedicin.pharmaceuticl=Pharmaceuticl.objects.get(pk=pharmaceuticl)
            formMedicin.patient=patient
            formMedicin.doctor=doctor
            formMedicin.save()
            return redirect(viewPationD,id)
    report=Report.objects.all()
    # pharmaceutic=MedicineModelForm.objects.all()

    return render(req,"Doctor/Manage/SinglePatient.html",{"patient":patient,"form":form,"report":report,'test':test,"doctor":doctor,"formMedicin":formMedicin})
@login_required
def doctorProfile(req):
    doctor=Doctor.objects.get(pk=req.user.id)
    form=CabilAuthorisedForm(req.POST or None)
    cabil=CABIL.objects.all()
    if req.method =="POST":
        if form.is_valid():
            cabilNumber=req.POST.get("cabilNumber")
            form=CabilAuthorised()
            form.doctor_no=doctor
            form.cableNumber=CABIL.objects.get(pk=cabilNumber)
            form.isAvailable=False
            form.save()
            return redirect(viewDoctor,id)
    
    cabilAprove=CabilAuthorised.objects.get(doctor_no=doctor.id)
    # cabilAprove=CabilAuthorised.objects.all()
    return render(req,"doctor/doctorProfile.html",{"doctor":doctor,"form":form,"cabil":cabil,"cabilAprove":cabilAprove})
@login_required
def viewReportD(req,id):
    report=Report.objects.get(pk=id)
    form = EditReportForm(req.POST or None,req.FILES or None,instance=report)
    if req.method=="POST":
        if form.is_valid():
            form=report
            form.action=True
            form.save()
            return redirect(viewReportD,id)
    return render(req,"Doctor/Manage/report.html",{"form":form,"report":report})

def medicine(req):
    form=PharmaceuticlForm(req.POST or None)
    data={}
    data['title']="Pharmaceuticl Details"
    data['form']=form
    if req.method=="POST":
        if form.is_valid():
            form.isAvailable=True
            form.save()
            return redirect(medicine)
    data['pharmaceuticl']=Pharmaceuticl.objects.all()
    return render(req,"Admin/Manage/other/pharmaceuticl.html",data)
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