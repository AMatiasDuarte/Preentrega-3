from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    carousel_caption_title= models.CharField(max_length=100)
    carousel_caption_description= models.CharField(max_length=500)
    heading= models.CharField(max_length=50)
    description= models.CharField(max_length=250)
    publisher= models.ForeignKey(to= User, on_delete= models.CASCADE, related_name="publisher")
    imagen = models.ImageField(upload_to= "posts", null= True, blank= True)
    
    def __str__(self):
        return f"{self.id} - {self.heading}"
    
    
class Profile(models.Model):
    user= models.OneToOneField(to= User, on_delete=models.CASCADE, related_name="profile")
    imagen = models.ImageField(upload_to= "profiles", null= True, blank= True)
    
    
    
