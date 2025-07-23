from django.urls import path
from .views import *
from . import views
urlpatterns=[
    path('students/',views.Students.as_view()),
    path('student/<int:pk>/',views.StudentDetails.as_view()),
    path('courses/',views.Courses.as_view()),
    path('course/<int:pk>',views.CourseDetails.as_view()),
    path('departments/',views.Departments.as_view()),
    path('department/',views.DepartmentDetails.as_view())
]