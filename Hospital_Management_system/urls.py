from django.contrib import admin
from django.urls import path
from Hospital.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("about/",about,name="about"),
    path("new-patient/",newPatient,name="newPatient"),
    path("logout/",logout,name="logout"),
    path("login/",login,name="login"),
    path("newDoctor/",newDoctor,name="newDoctor"),
    path("admin-home/",adminHome,name="dashboard"),
    path("manage-Old-Doctor/",manageOldDoctor,name="manageOldDoctor"),
    path("manage-New-Doctor/",manageNewDoctor,name="manageNewDoctor"),
    path("approve-doctor/<int:id>/approve/",approveDoctor,name="approveDoctor"),
    path("single-view-doctor/<int:id>/view/",viewDoctor,name="viewDoctor"),
    path("delete-old-doctor-details/<int:id>/delete/",deleteDoctor,name="deleteDoctor"),
    path("edit-old-doctor-details/<int:id>/delete/",editDoctor,name="editDoctor"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)