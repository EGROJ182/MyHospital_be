from django.contrib import admin
from .models.user import User
from .models.patient import Patient
from .models.doctor import Doctor

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)