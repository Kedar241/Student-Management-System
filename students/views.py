from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Student, Teacher, Course
from .forms import StudentForm, TeacherForm, CourseForm


# HOME: Display dashboard

@login_required
def home(request):
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    total_courses = Course.objects.count()

    recent_students = Student.objects.order_by('-enrollment_date')[:5]

    context = {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_courses': total_courses,
        'recent_students': recent_students,
    }

    return render(request, 'students/home.html', context)



# READ: Display all students
@login_required
def student_list(request):
    students = Student.objects.all()

    return render(request, 'students/student_list.html', {
        'students': students
    })


# CREATE: Add a new student
@login_required
def student_create(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {
        'form': form,
        'title': 'Add Student'
    })


# UPDATE: Edit an existing student
@login_required
def student_update(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_form.html', {
        'form': form,
        'title': 'Update Student'
    })


# DELETE: Remove a student
@login_required
def student_delete(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'students/student_confirm_delete.html', {
        'student': student
    })
    

# USER REGISTRATION
def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {
        'form': form
    })
    

# TEACHER: Display all teacher
@login_required
def teacher_list(request):
    teachers = Teacher.objects.all().order_by('full_name')
    
    return render(request, 'students/teacher_list.html', {
        'teachers': teachers
    })
    

# TEACHER: Add a new teacher
@login_required
def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
        
        
    return render(request, 'students/teacher_form.html', {
        'form': form,
        'title': 'Add Teacher'
    })
    
    
# TEACHER: Update teacher details
@login_required
def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
        
    return render(request, 'students/teacher_form.html', {
        'form': form,
        'title': 'Update Teacher'
    })


# TEACHER: Delete a teacher
@login_required
def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    
    return render(request, 'students/teacher_confirm_delete.html', {
        'teacher': teacher
    })
    

# COURSE: Display all courses
@login_required
def course_list(request):
    courses = Course.objects.select_related('teacher').all().order_by('course_name')
    
    return render(request, 'students/course_list.html', {
        'courses': courses
    })
    
    
# COURSE: Add a new course
@login_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
        
    return render(request, 'students/course_form.html', {
        'form': form,
        'title': 'Add Course'
    })
    
# COURSE:Update course details
@login_required
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
        
    return render(request, 'students/course_form.html', {
        'form': form,
        'title': 'Update Course'
    })
    
# COURSE: Delete a course
@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    
    return render(request, 'students/course_confirm_delete.html', {
        'course': course
    })
    
    