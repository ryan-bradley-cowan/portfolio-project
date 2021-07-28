from django.shortcuts import render

#required to convert postgresql to python objects
from .models import Job

def home(request):
    jobs = Job.objects #converts postgresql to python objects
    return render(request, 'jobs/home.html', {'jobs':jobs})
