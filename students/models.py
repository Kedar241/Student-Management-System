from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    enrollment_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name
    

# Teacher model
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    specialization = models.CharField(max_length=100, blank=True)
    hire_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.full_name
    

# Course model
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    duration = models.CharField(max_length=50)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        related_name='courses'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.course_name
    