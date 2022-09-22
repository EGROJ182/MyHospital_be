from django.db import models
from .user import User

class Doctor(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, related_name='doctor', on_delete=models.CASCADE)
    specialty=models.CharField('Specialty', max_length=50)