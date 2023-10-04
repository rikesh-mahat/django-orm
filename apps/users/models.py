from django.db import models

# Create your models here.

class CommonInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    
class Teacher(CommonInfo):
    pass
    
class Student(CommonInfo):
    age = models.IntegerField()
    classroom = models.IntegerField()
    
    # incase if you want to override the meta method of the base class
    # class Meta(CommonInfo.Meta):
    #     ordering = ['first_name']
    
    
'''
class Books(models.Model):
    title = models.CharField(max_length = 200)
    price = models.FloatField()
    
    
class ISBN(Books):
    isbn = models.CharField(max_length=16)
    
# in other way

class ISBN(models.Model):
    book = models.OneToOneField(Books, on_delete=models.CASCADE)
    isbn = models.CharField(max_length = 16)
    
    
# when you create an instance of the isbn model books instance will be automatically created 
'''
    
class Books(models.Model):
    title = models.CharField(max_length = 200)
    price = models.FloatField()
    
    
    def __str__(self):
        return self.title
    
class ISBN(Books):
    isbn_number = models.CharField(max_length=16)
    
