from django.contrib import admin
from Education.models import BaseUser, Course, Lecture


@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'level')


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
