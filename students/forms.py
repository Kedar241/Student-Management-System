from django import forms
from .models import Student

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