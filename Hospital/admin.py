from django.contrib import admin
from .models import * 
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Room)
admin.site.register(Bill)
admin.site.register(Report)
admin.site.register(CABIL)