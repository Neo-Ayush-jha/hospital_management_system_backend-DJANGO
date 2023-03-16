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
    path("manage-patient/",managePation,name="managePation"),
    path("manage-room/",roomDetails,name="roomDetails"),
    path("manage-cabil/",cabilDetails,name="cabilDetails"),
    path("manage-test/",tests,name="tests"),
    path("manage-old-patient/",manageOldPation,name="manageOldPation"),
    path("manage-Old-Doctor/",manageOldDoctor,name="manageOldDoctor"),
    path("manage-New-Doctor/",manageNewDoctor,name="manageNewDoctor"),
    path("approve-doctor/<int:id>/approve/",approveDoctor,name="approveDoctor"),
    path("single-view-doctor/<int:id>/view/",viewDoctor,name="viewDoctor"),
    path("single-view-patient/<int:id>/view/",viewPation,name="viewPation"),
    path("single-view-patient-report/<int:id>/",viewReport,name="viewReport"),
    path("delete-old-doctor-details/<int:id>/delete/",deleteDoctor,name="deleteDoctor"),
    path("edit-old-doctor-details/<int:id>/edit/",editDoctor,name="editDoctor"),
    path("edit-patient-details/<int:id>/edit/",editPation,name="editPation"),
    path("edit-room-details/<int:id>/edit/",editRoomDetails,name="editRoomDetails"),
    path("edit-cabil-details/<int:id>/edit/",editCabilDetails,name="editCabilDetails"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)