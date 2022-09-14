from sys import stderr
from django.contrib import admin
from .models import Student_Three

# Register your models here.

@admin.register(Student_Three)
class StudentAdmin(admin.ModelAdmin):
    list_display= ['id', 'name', 'roll', 'city']