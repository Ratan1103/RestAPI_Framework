from rest_framework import serializers
from .models import Course,Department,Student

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Course
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(source='course', many=True, read_only=True)
    
    course_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Course.objects.all(),
        write_only=True,
        source='course'
    )

    class Meta:
        model = Student
        fields = ['id', 'std_id', 'std_name', 'department', 'courses', 'course_ids']
    
class DepartmentSerializer(serializers.ModelSerializer):
    students=StudentSerializer(many=True,read_only=True)
    class Meta:
        model=Department
        fields='__all__'



