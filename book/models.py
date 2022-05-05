from django.db import models
   
class Writer(models.Model):
    name=models.CharField(max_length=40)
    
    def __str__(self) -> str:
        return self.name
    
class Book(models.Model):
    name=models.CharField(max_length=100)
    writer = models.ForeignKey(Writer,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name