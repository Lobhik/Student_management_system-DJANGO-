from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student
from .forms import StudentForm

# Create your views here.
def index(request):
  return render(request, 'students/index.html', {
    'students': Student.objects.all()
  })

def view_student(request, id):
  student = Student.objects.get(pk=id)
  return HttpResponseRedirect(reverse('index'))

def add(request):
  # if this is a POST request we need to process the form data

  if request.method == 'POST':
    # create a form instance and populate it with data from the request:

    form = StudentForm(request.POST)
    # check whether it's valid:

    if form.is_valid():
      # process the data in form.cleaned_data as required

      new_student_number = form.cleaned_data['student_number']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      new_field_of_study = form.cleaned_data['field_of_study']
      new_gpa = form.cleaned_data['gpa']

      new_student = Student(
        student_number = new_student_number,
        first_name = new_first_name,
        last_name = new_last_name,
        email = new_email,
        field_of_study = new_field_of_study,
        gpa = new_gpa
      )
      #saving the Form
      new_student.save()
      # redirect to a new URL:
      return render(request, 'students/add.html', {
        'form': StudentForm(),
        'success': True
      })
  # if a GET (or any other method) we'll create a blank form
  else:
    form = StudentForm()
  return render(request, 'students/add.html', {
    'form': StudentForm()
  })
#update the student
def edit_student(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      #saving the data to database
      form.save()

      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })
#delete the student
def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))