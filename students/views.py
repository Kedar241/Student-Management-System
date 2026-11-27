from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Student
from .forms import StudentForm


# HOME: Display dashboard
@login_required
def home(request):

    total_students = Student.objects.count()

    recent_students = Student.objects.order_by(
        '-enrollment_date'
    )[:5]

    context = {
        'total_students': total_students,
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
