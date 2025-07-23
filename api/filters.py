import django_filters
from students.models import Student,Course,Department

class StudentFilter(django_filters.FilterSet):
    department = django_filters.CharFilter(field_name='department__dept_name',lookup_expr='iexact')
    course = django_filters.CharFilter(field_name='course__course_name',lookup_expr='iexact')
    class Meta:
        model = Student
        fields = ['department','course']