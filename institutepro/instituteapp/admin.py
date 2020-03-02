from django.contrib import admin
from .models import CoursesData


class AdminCoursesData(admin.ModelAdmin):
    list_display = ['course_name', 'duration', 'start_date', 'start_time', 'trainer_name', 'trainer_exp', 'content']


admin.site.register(CoursesData, AdminCoursesData)
