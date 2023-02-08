from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone
from django.views.generic.edit import CreateView
from .models import Appointment, Coach
from django.views.generic import TemplateView
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
    
@login_required
def home(request):
	context ={
	'notes': Coach.objects.all()
	}
	return render(request, 'home.html',context)