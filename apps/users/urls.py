from django.urls import path
from apps.users.views import student, teachers

urlpatterns = [
    path('students/', student),
    path('teachers/', teachers),
]
