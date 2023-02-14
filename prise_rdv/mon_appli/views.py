from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone
from django.views.generic.edit import CreateView
from .models import Appointment, Coach
from .forms import AppointmentForm
from django.views.generic import TemplateView
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from datetime import datetime
from datetime import timedelta
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'home.html')

class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        print("Appointment: form_valid")
        appointment = form.save(commit=False)
        appointment.client = self.request.user
        start = datetime.combine(appointment.date, appointment.start_time)
        end = start + appointment.duration
        existing_appointments = Appointment.objects.filter(
            date=appointment.date,
            start_time__lt=end + timedelta(minutes=10),
            start_time__gte=start
        )
        if existing_appointments.exists():
            raise ValidationError("An appointment already exists during that time")
        appointment.save()
        print("Appointment created successfully")
        return super().form_valid(form)
    
@login_required
def appointments_history(request):
    user = request.user
    appointments = Appointment.objects.filter(client=request.user)
    context = {'appointments': appointments}
    return render(request, 'appointments/appointments_history.html', context)
    

