from django.db import models
from users.models import *
from django.utils import timezone
import pytz

STATUS_CHOICES = (
    ("1", "ONGOING"),
    ("2", "CLOSED"),
    ("3", "TERMINATED")
)
class session(models.Model):
    s_id = models.AutoField(primary_key=True)
    user_id=models.ForeignKey(teacher,on_delete=models.CASCADE, default=None)
    start_time= models.DateTimeField(default=timezone.now)
    end_time= models.DateTimeField(default=None)
    status=models.CharField(max_length=100,choices=STATUS_CHOICES,default=1)
    session_key=models.CharField(max_length=100,default=None)
    


    
