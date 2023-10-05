from django.contrib import admin
from apps.users.models import Student, Teacher, Author, Blog, Publishers, Products
# Register your models here.

admin.site.register([Student, Teacher, Author, Blog, Publishers, Products])
