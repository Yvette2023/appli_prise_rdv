from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone
from django.views.generic.edit import CreateView
from .models import Appointment, Coach
from django.views.generic import TemplateView
    
def home(request):
	context ={
	'notes': Coach.objects.all()
	}
	return render(request, 'home.html',context)