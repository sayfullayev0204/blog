from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField()
    img = models.ImageField(upload_to='img/')
    t_yil = models.DateField()
