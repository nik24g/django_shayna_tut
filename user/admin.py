from django.contrib import admin
from user.models import Contact, Student, Employee

# Register your models here.
admin.site.register(Contact)
admin.site.register(Student)
admin.site.register(Employee)