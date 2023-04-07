from django.db import models

class Post(models.Model):
    Title_Post= models.CharField(max_length=100)
    Description_Post= models.CharField(max_length=500)
    Trekk_Post= models.CharField(max_length=50)
    Description_Trekk_Post= models.CharField(max_length=250)
    
    def __str__(self):
        return f"{self.id} - {self.Trekk_Post}"
    
    
        
    
    
