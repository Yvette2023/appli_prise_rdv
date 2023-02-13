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
  
class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['client', 'date', 'start_time', 'session_object']
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointments:list')

    def form_valid(self, form):
        coach = Coach.objects.first()  # Obtenir le seul coach disponible dans la table
        appointment = form.save(commit=False)
        appointment.coach = coach  # Définir le coach pour le rendez-vous
        start_time = appointment.start_time
        date = appointment.date
        end_time = timezone.make_aware(timezone.datetime.combine(date, start_time) + appointment.duration)
        overlapping_appointments = Appointment.objects.filter(
            coach=appointment.coach,
            start_time__range=(start_time, end_time))
        if overlapping_appointments.exists():
            messages.error(self.request, "Le coach est déjà réservé à ce moment-là")
            return render(self.request, 'appointments/appointment_form.html', {'form': form})

        ten_minutes = timezone.timedelta(minutes=10)
        previous_appointment = Appointment.objects.filter(
            coach=appointment.coach,
            start_time__lt=start_time,
            start_time__gte=start_time - ten_minutes).last()
        if previous_appointment:
            messages.error(self.request, "Il doit y avoir au moins 10 minutes entre deux rendez-vous")
            return render(self.request, 'appointments/appointment_form.html', {'form': form})

        next_appointment = Appointment.objects.filter(
            coach=appointment.coach,
            start_time__gt=start_time,
            start_time__lte=start_time + ten_minutes).first()
        if next_appointment:
            messages.error(self.request, "Il doit y avoir au moins 10 minutes entre deux rendez-vous")
            return render(self.request, 'appointments/appointment_form.html', {'form': form})
        
        appointment.save()
        messages.success(self.request, "Votre rendez-vous a été enregistré avec succès")
        return redirect(self.success_url)

       # appointment.save()
        # return super().form_valid(form)   
   
def appointments_history(request):
    appointments = Appointment.objects.all()
    context = {'appointments': appointments}
    return render(request, 'appointments/appointments_history.html', context)

