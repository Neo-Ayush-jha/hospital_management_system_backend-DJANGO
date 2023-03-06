from django.contrib import admin
from django.urls import path
from Hospital.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("about/",about,name="about"),
    path("new_patient",newPatient,name="newPatient"),
    path("logout",logout,name="logout"),
    path("newDoctor",newDoctor,name="newDoctor"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)