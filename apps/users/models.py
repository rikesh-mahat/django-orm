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
    

    


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length= 5, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Publishers(models.Model):
    name = models.CharField(max_length=100)
    blogs = models.ManyToManyField(Blog)
    
    def __str__(self):
        return self.name
    
    
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name