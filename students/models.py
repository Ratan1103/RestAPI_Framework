from django.db import models

# Create your models here.

class Course(models.Model):
    course_id=models.CharField(max_length=20)
    course_name=models.CharField(max_length=50)

    def __str__(self):
        return self.course_name
    

class Department(models.Model):
    dept_id=models.CharField(max_length=20)
    dept_name=models.CharField(max_length=50)

    def __str__(self):
        return self.dept_name
    

class Student(models.Model):
    std_id=models.CharField(max_length=20)
    std_name=models.CharField(max_length=50)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name='students')
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        return self.std_name
    

