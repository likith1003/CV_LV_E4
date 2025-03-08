from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
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
    success_url = 'cbv_school'

class list_schools(ListView):
    model = School
    context_object_name = 'schools'
    ordering = ['sname']