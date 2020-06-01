from django.contrib import admin

from Education.models import Course, Lecture


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'level')


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
