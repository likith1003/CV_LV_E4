from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
# Create your views here.


def fbv_school(request):
    ESFO = SchoolForm()
    d = {'ESFO': ESFO}
    if request.method == 'POST':
        SFDO = SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Done....')
    return render(request, 'fbv_school.html', d)


class cbv_school(CreateView):
    model = School
    fields='__all__'
    success_url = 'list_schools'

class list_schools(ListView):
    model = School
    context_object_name = 'schools'
    ordering = ['sname']


class Addstd(CreateView):
    model = Student
    fields = '__all__'
    success_url = 'list_schools'

class viewschool(DetailView):
    model = School
    context_object_name = 'school'

class update_school(UpdateView):
    model = School
    fields = '__all__'
    success_url = 'list_schools'

class delete_school(DeleteView):
    model = School
    success_url = 'list_schools'
    context_object_name = 'school'