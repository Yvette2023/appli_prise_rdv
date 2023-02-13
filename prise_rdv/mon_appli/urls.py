from django.urls import path
from mon_appli import views

urlpatterns = [
    path('',views.home, name='home'),
]