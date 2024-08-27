from django.db import models

# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField(null=True, blank=True)
    status=models.CharField(max_length=50, null=True, blank=True)