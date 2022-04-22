import email
from django.db import models


# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length = 100)
    
    def __str__(self):
        return f"{self.author_name}"

class Category(models.Model):
    category = models.CharField(max_length=100)
    location = models.IntegerField(max_length = 100)
    
    def __str__(self):
        return f"{self.category}"
        


class Books(models.Model):
    book_name = models.CharField(max_length  = 100,null = False)
    author_name = models.ForeignKey(Author,on_delete=models.CASCADE)
    ISBN = models.IntegerField(max_length = 100, unique=True)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.book_name}, {self.ISBN}, {self.quantity}"
    

# class Staffid(models.model):
#     username = models.CharField(max_length=44,unique=True)
#     email = models.EmailField(max_length= 100,unique=True)
#     pass1 = models.CharField(max_length = 16)
    