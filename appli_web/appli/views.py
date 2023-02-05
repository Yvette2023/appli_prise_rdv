from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone
from django.views.generic.edit import CreateView
from .models import Appointment

class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['client', 'coach', 'date', 'start_time', 'session_object']
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointments:list')

    def form_valid(self, form):
        appointment = form.save(commit=False)
        start_time = appointment.start_time
        date = appointment.date
        end_time = timezone.make_aware(timezone.datetime.combine(date, start_time) + appointment.duration)
        overlapping_appointments = Appointment.objects.filter(
            coach=appointment.coach,
            start_time__range=(start_time, end_time)
        )
        if overlapping_appointments.exists():
            messages.error(self.request, "Coach is already booked at this time")
            return render(self.request, 'appointments/appointment_form.html', {'form': form})

        ten_minutes = timezone.timedelta(minutes=10)
        previous_appointment = Appointment.objects.filter(
            coach=appointment.coach,
            start_time__lt=start_time,
            start_time__gte=start_time - ten_minutes
        ).last()
        if previous_appointment:
            messages.error(self.request, "There should be at least 10 minutes between two appointments")
            return render(self.request, 'appointments/appointment_form.html', {'form': form})

        next_appointment = Appointment.objects.filter(
            coach=appointment.coach,
            start_time__gt=start_time,
            start_time__lte=start_time + ten_minutes
        ).first()
        if next_appointment:
            messages.error(self.request, "There should be at least 10 minutes between two appointments")
            return render(self.request, 'appointments/appointment_form.html', {'form': form})

        appointment.save()
        return super().form_valid(form)

