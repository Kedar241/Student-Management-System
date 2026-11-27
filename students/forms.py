
from django import forms
from .models import Student, Teacher, Course


# Student Form
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'full_name',
            'email',
            'phone_number',
            'date_of_birth',
            'address',
        ]


# Teacher Form
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher

        fields = [
            'full_name',
            'email',
            'phone_number',
            'specialization',
            'hire_date',
        ]

        widgets = {
            'hire_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }
        

# Course Form
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'course_name',
            'course_code',
            'description',
            'duration',
            'teacher',
        ]
