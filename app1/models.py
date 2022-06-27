from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookEntry(models.Model):
    
    name=models.CharField(max_length=30)
    isbn=models.PositiveIntegerField()
    author=models.CharField(max_length=40)
    library_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+']'