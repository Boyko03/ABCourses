from django.contrib import admin
from Education.models import BaseUser, Teacher, Student


@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ('user_name')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
