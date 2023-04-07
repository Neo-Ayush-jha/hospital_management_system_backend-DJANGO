from django.contrib import admin
from django.urls import path
from Hospital.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("health/",health,name="health"),
    path("new-patient/",newPatient,name="newPatient"),
    path("logout/",logout,name="logout"),
    path("login/",login,name="login"),
    path("newDoctor/",newDoctor,name="newDoctor"),
    path("admin-home/",adminHome,name="dashboard"),
    path("manage-room/",roomDetails,name="roomDetails"),
    path("manage-cabil/",cabilDetails,name="cabilDetails"),
    path("manage-cabil/doctor-view/",cabilDetailsD,name="cabilDetailsD"),
    path("manage-test/",tests,name="tests"),
    path("manage-patient/",managePation,name="managePation"),
    path("manage-old-patient/",manageOldPation,name="manageOldPation"),
    path("doctor/manage-patient/",managePationD,name="managePationD"),
    path("doctor/manage-old-patient/",manageOldPationD,name="manageOldPationD"),
    path("manage-Old-Doctor/",manageOldDoctor,name="manageOldDoctor"),
    path("manage-New-Doctor/",manageNewDoctor,name="manageNewDoctor"),
    path("approve-doctor/<int:id>/approve/",approveDoctor,name="approveDoctor"),
    path("single-view-doctor/<int:id>/view/",viewDoctor,name="viewDoctor"),
    path("single-view-patient/<int:id>/view/",viewPation,name="viewPation"),
    path("doctor/single-view-patient/<int:id>/",viewPationD,name="viewPationD"),
    path("doctor/single-view-patient/<int:id>/pharmaceutic/",pharmaceutic,name="pharmaceutic"),

    path("single-view-patient-report/<int:id>/",viewReport,name="viewReport"),
    path("delete-old-doctor-details/<int:id>/delete/",deleteDoctor,name="deleteDoctor"),
    path("edit-old-doctor-details/<int:id>/edit/",editDoctor,name="editDoctor"),
    path("edit-patient-details/<int:id>/edit/",editPation,name="editPation"),
    path("edit-room-details/<int:id>/edit/",editRoomDetails,name="editRoomDetails"),
    path("edit-cabil-details/<int:id>/edit/",editCabilDetails,name="editCabilDetails"),
    path("doctor-dashboard/",doctorDashboard,name="doctorDashboard"),
    path("doctor-my-proflie/view/",doctorProfile,name="doctorProfile"),
    path("doctor/single-view-patient-report/<int:id>/",viewReportD,name="viewReportD"),
    path("manage-pharmaceutical/",medicine,name="medicine"),
    path("staff-view/form/",StaffView.as_view(),name="StaffView"),
    path("bill-view/form/",BillView.as_view(),name="BillView"),
    path("notification/",NotificationView.as_view(),name="NotificationView"),
    path("doctor/notification/",DoctorMessage.as_view(),name="DoctorMessage"),
    path("staff/leave/",Staff_leaveView.as_view(),name="Staff_leaveView"),
    path("staff/leave/<int:id>/",staff_leave_approve,name="staff_leave_approve"),
    path("doctor/leave/",doctor_leaveView,name="doctor_leaveView"),
    path('check/appointment/', appointment, name='appointment'),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)