from django.test import TestCase

# Create your tests here.
# from datetime import time, timedelta
# from celery.decorators import periodic_task
# from celery.task.schedules import crontab
# from .models import Attendance

# @periodic_task(run_every=crontab(hour=0, minute=0))
# def reset_attendance_status():
#     profiles = Attendance.objects.all()
#     for profile in profiles:
#         profile.is_present = False
#         profile.save()