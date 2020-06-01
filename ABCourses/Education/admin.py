from django.contrib import admin
from Education.models import BaseUser, Teacher, Student, Course, Lecture


@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ('user_name', )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'level')


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
