from django.shortcuts import render
from apps.users.models import Student, Teacher
# Create your views here.
def student(request):
    context = {}
    context['students'] = Student.objects.all()
    
    return render(request, 'students.html', context)


def teachers(request):
    context  = {}
    return render(request, 'teachers.html', context)


'''
 rest of the code will be running on python shell
 
 
 commands : 
 
 # open shell in the terminal
 - python manage.py shell
 
 # import the models 
 - from apps.users.models import *
 
 # get student data
 - students = Student.objects.all()
 - students
 
 # get a specific student data
 - first_student = Student.object.get(id=1)
 - first_student
 
 # filter using specific name
 - student = Student.objects.filter(name="benny")
 - student
 
 # things we can use with filter()
 - exact: Matches the exact value of a field.
 - iexact: Case-insensitive exact match.
 - contains: Matches if the field contains the specified value.
 - icontains: Case-insensitive version of contains.
 - startswith: Matches if the field starts with the specified value.
 - istartswith: Case-insensitive version of startswith.
 - endswith: Matches if the field ends with the specified value.
 - iendswith: Case-insensitive version of endswith.
 - in: Matches if the field value is in a given list.
 - gt: Greater than.
 - lt: Less than.
 - gte: Greater than or equal to.
 - lte: Less than or equal to.
 - range: Matches if the field value falls within a specified range.
 - isnull: Matches if the field is NULL or None.
 - regex: Matches using a regular expression.

# continuation to our filter query
- student = Student.objects.filter(first_name__startswith='jh')  
- student
- student = Student.objects.filter(last_name__endwith = 'al')
- student
- student = Student.objects.filter(first_name__icontains = 'ja')
- student
- id_list = [1,2]
- students = Student.objects.filter(id__in = id_list)
- students = Student.objects.filter(age__gt = 14)
- students
- students = Student.objects.filter(age__lte = 12) 
- students
- students = Student.objects.filter(age__range = (10, 15))
- students
- email_pattern = r'@example\.com$'
- students = Student.objects.filter(email__regex = email_pattern)

# OR, AND and NOT query in django ORM
- from django.db.models import Q

# OR
- students = Student.objects.filter(Q(first_name__iexact = 'john') | Q(last_name__iexact = 'cena'))
- students

# AND
- students = Student.objects.filter(Q(first_name__iexact = 'john') & Q(last_name__iexact = 'cena'))
- students

# NOT
- students = Student.objects.filter(Q(first_name__iexact = 'john') | ~Q(last_name__iexact = 'cena'))
- students

# UNION using django orm

# simple way
- query_1 = Student.object.all().value_list('first_name')
- query_2 = Teacher.object.all().value_list('first_name')
- combined_query = query_1 | query_2

- data = Student.objects.all().values('first_name').union(Teacher.objects.all().values('last_name'))
- data

# only 
- name = Student.objects.filter(id=1).only('first_name', 'last_name)

# using raw sql query
- students = Student.objects.raw("SELECT * FROM student_student") # returns raw queryset

# pure raw sql query without using django orm
- from django.db import connection
- cursor = connection.cursor()
- cursor.execute("SELECT count(*) FROM student_student")
- result = cursor.fetchone()

# you can use fetch all as well
- cursor.execute("SELECT * FROM student_student")
- result = cursor.fetchall() # returns a list of tuple


# aggregate and annotate
- from django.db.models import Count, Sum, Avg, Min, Max
- total_price = Products.objects.aggregate(Sum('price'))['price__sum']
// without using ['price__sum'] -> output : {'price__sum' : numbers} else numbers
- min_price = Products.objects.aggrgate(Avg('price'))['price__min']
- max_price = Products.objects.aggregate(Max('price'))['price__max']

- publisher = Publisher.objects.annotate(blogs_count = Count('blogs'))
- publisher = Publisher.objects.filter(name__iexact = "E.R Clark").annotate(blogs_count = Count('blogs))

# select_related and prefetch_related

# select_related(one-to-many/foreign key, one-one)

- data = Blog.objects.select_related("author").all()
- data[0].author   # immediately available no later sql trigger due to inner join
- data = Blog.objects.all()
- data = data[0].author # sql query triggered

- data = Blog.objects.select_related('author').all()

# prefetch_related(reverse foreign_key & many-to-many relationship)

authors = Author.objects.prefetch_related('blog_set').all()
publishers = Publishers.objects.prefetch_related('blogs').all()


'''