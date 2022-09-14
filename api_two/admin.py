from django.contrib import admin
from .models import Student_Two
# Register your models here.

@admin.register(Student_Two)
class StudentTwoAdmin(admin.ModelAdmin):
    list_display= ['id', 'name','roll', 'city']
    