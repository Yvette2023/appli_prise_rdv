from django.contrib import admin

# Register your models here.

from .models import Coach

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

