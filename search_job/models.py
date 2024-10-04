from django.db import models
from django.contrib.auth.models import User


# User Model
class ProfileUser(models.Model):
    gender_list =[  
          ('Male' ,'Male'),
          ('Female' ,'Female'),
    ]
    qualification_list=[
        ('UG','UG'),
        ('PG','PG'),
    ]
    
    username = models.OneToOneField(User ,on_delete=models.CASCADE)
    pro_image = models.ImageField()
    contact= models.CharField(max_length=10)
    gender = models.CharField(choices=gender_list ,max_length=10)
    qualification=models.CharField(choices=qualification_list ,max_length=10)