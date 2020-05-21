from django.db import models
from django.utils import timezone
import pytz


STATUS_CHOICES = (
    ("1", "ACTIVE"),
    ("2", "INACTIVE")
)

STATUS_CHOICES = (
    ("1", "ACTIVE"),
    ("2", "INACTIVE")
)
class teacher(models.Model):
    t_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    passwd = models.CharField(max_length=100, blank=True)
    added_date = models.DateTimeField(default=timezone.now)
    added_by = models.CharField(max_length=100, default=None)
    last_modified_date = models.DateTimeField(default=timezone.now)
    last_modified_by = models.CharField(
        max_length=100, default=None, null=True)
    status=models.CharField(max_length=100,choices=STATUS_CHOICES,default=1)


class course(models.Model):
    c_id = models.AutoField(primary_key=True)
    course_code = models.CharField(max_length=100, default=None)
    class_count = models.IntegerField(default=0)
    enrolled_students_list = models.FileField(upload_to='studentList/')
    added_date = models.DateTimeField(default=timezone.now)
    added_by = models.CharField(max_length=100, default=None)
    last_modified_date = models.DateTimeField(default=timezone.now)
    last_modified_by = models.CharField(
        max_length=100, default=None, null=True)
    status=models.CharField(max_length=100,choices=STATUS_CHOICES,default=1)
