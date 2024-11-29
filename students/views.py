from django.shortcuts import render
from .models import Student


def student_list(request):
    first_name = request.GET.get('firstName')
    last_name = request.GET.get('lastName')
    email = request.GET.get('email')
    age = request.GET.get('age')
    if first_name is not None and last_name is not None and email is not None and age is not None:
        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            age=age
        )
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/student_list.html', ctx)
