from django.db import models
from .user import User
from .doctor import Doctor

class Patient(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, related_name='patient', on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor, related_name='patient', on_delete=models.CASCADE)