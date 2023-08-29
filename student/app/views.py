from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .forms  import StudentForm
from .models import Student

def Home(request):
    return render(request,'home.html')


class StudentCreate(generic.CreateView):
    model = Student
    fields = '__all__'
    template_name = 'student_register_form.html'
    success_url = "/studentlist"




class StudentList(generic.ListView):
    template_name = 'student_list.html'
    model = Student


