from django.db import models

class Post(models.Model):
    carousel_caption_title= models.CharField(max_length=100)
    carousel_caption_description= models.CharField(max_length=500)
    heading= models.CharField(max_length=50)
    description= models.CharField(max_length=250)
    
    def __str__(self):
        return f"{self.id} - {self.heading}"
    
    
        
    
    
