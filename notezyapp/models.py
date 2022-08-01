from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class note(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()
    user= models.ForeignKey(to=User, on_delete=models.CASCADE ,null=True,blank=True)

