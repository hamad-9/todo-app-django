from django.db import models

# Create your models here.
class Tasks(models.Model):
    description =  models.CharField(max_length=255)
    isDon = models.BooleanField(default=False)