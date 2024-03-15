from django.db import models

# Create your models here.
class apii(models.Model):
    title= models.CharField(max_length=150)
    description= models.TextField()
    date=models.DateField(auto_now_add=True)
