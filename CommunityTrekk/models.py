from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    principal_title= models.CharField(max_length=100)
    principal_description= models.CharField(max_length=500)
    heading= models.CharField(max_length=50)
    description= models.CharField(max_length=250)
    created_the= models.DateTimeField(auto_now_add= True)
    publisher= models.ForeignKey(to= User, on_delete= models.CASCADE, related_name="publisher")
    imagen = models.ImageField(upload_to= "posts", null= True, blank= True)
    imagen2 = models.ImageField(upload_to= "posts", null= True, blank= True)
    imagen3 = models.ImageField(upload_to= "posts", null= True, blank= True)
    trekk_value= models.CharField(max_length=10, default= "$0")
    trekk_duration= models.CharField(max_length=20, default= "1 día")
        
    
    def __str__(self):
        return f"{self.id} - {self.heading}"
    
    
class Profile(models.Model):
    user= models.OneToOneField(to= User, on_delete=models.CASCADE, related_name="profile")
    imagen = models.ImageField(upload_to= "profiles", null= True, blank= True)
    
    
    
