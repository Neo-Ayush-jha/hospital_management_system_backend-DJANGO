from django.contrib import admin
from .models import * 
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Room)
admin.site.register(Bill)
admin.site.register(Report)
admin.site.register(CABIL)
admin.site.register(Test)
admin.site.register(CabilAuthorised)
admin.site.register(Pharmaceuticl)
admin.site.register(MedicineModel)
admin.site.register(Payment)