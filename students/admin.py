from django.contrib import admin
from .models import Student,Course,Department

# Register your models here.

admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Course)
