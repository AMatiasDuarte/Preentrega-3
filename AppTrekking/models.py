from django.db import models

class Trekking(models.Model):
    nombre = models.TextField(max_length=100)
    estado = models.TextField(max_length=100)   
    creado = models.DateTimeField(auto_now_add="")
    modificado = models.DateTimeField(auto_now="")
    
    def terminar(self):
        self.estado = "Terminado"
        
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.estado}"
    
    
class Persona(models.Model):
    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100)
    dni = models.TextField(max_length=8)
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.apellido} - {self.dni}"
    
    
class Evento(models.Model):
    nombre = models.TextField(max_length=100)
    estado = models.TextField(max_length=100)
    creado = models.DateTimeField(auto_now_add="")
    modificado = models.DateTimeField(auto_now="")
    
    def concluir(self):
        self.estado = "Concluído"
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.estado}"
    
    

