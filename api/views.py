from django.shortcuts import render
from students.serializers import StudentSerializer,CourseSerializer,DepartmentSerializer
from rest_framework import generics
from students.models import Student,Course,Department
from .paginations import CustomPagination
from .filters import StudentFilter
class Students(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=CustomPagination
    filterset_class=StudentFilter

class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    lookup_field='pk'


class Courses(generics.ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

class CourseDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    lookup_field='pk'


class Departments(generics.ListCreateAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    
class DepartmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    lookup_field='pk'


    
