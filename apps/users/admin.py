from django.contrib import admin
from apps.users.models import Student, Teacher, Books, ISBN
# Register your models here.

admin.site.register([Student, Teacher, Books, ISBN])
