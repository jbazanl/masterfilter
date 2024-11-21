from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Permision(models.Model):
    movil = models.BooleanField(default=False)
    fijo = models.BooleanField(default=False)
    orange1 = models.BooleanField(default=False)
    orange2 = models.BooleanField(default=False)
    wsp = False
    abct = models.BooleanField(default=True)
    amarilla = models.BooleanField(default=True)
    infobel = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
    
class Document(models.Model):
    file = models.FileField(upload_to="subido")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)

class EndPoint(models.Model):
    movil = models.CharField(max_length=150)
    fijo = models.CharField(max_length=150)
    orange1 = models.CharField(max_length=150)
    orange2 = models.CharField(max_length=150)
    abct = models.CharField(max_length=150)
    wsp = models.CharField(max_length=150, null=True, blank=True)
    amarilla = models.CharField(max_length=150, null=True, blank=True)
    infobel = models.CharField(max_length=150, null=True, blank=True)