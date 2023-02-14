"""prise_rdv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from mon_appli import views as mon_appli_views, views
from django.urls import path, include
from mon_appli.views import AppointmentCreateView, appointments_history


urlpatterns = [
    path('', mon_appli_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('booking/', AppointmentCreateView.as_view(), name='create_appointment'),
    path('history/',appointments_history, name='appointments_history'),
    path('', include('usersapp.urls')),

]