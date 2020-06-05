from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


class BaseUser(models.Model):
    TEACHER = 'Teacher'
    STUDENT = 'Student'
    ROLES = [
        (TEACHER, TEACHER),
        (STUDENT, STUDENT)
    ]
    user_id = models.AutoField(primary_key=True, serialize=False, unique=True)
    name = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255, choices=ROLES, default=STUDENT)

    def __str__(self):
        return f'User {self.name}'


class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    # rating = models.FloatField
    BEGINER = 'Beginer'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'
    LEVELS = [
        (BEGINER, BEGINER),
        (INTERMEDIATE, INTERMEDIATE),
        (ADVANCED, ADVANCED)
    ]
    level = models.CharField(max_length=255, choices=LEVELS, default=BEGINER)

    def __str__(self):
        return f'{self.name}'


class Lecture(models.Model):
    def youtube_validator(url):
        if 'youtube.com' not in url:
            raise ValidationError('not a YouTube link')

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    url = models.URLField(validators=[URLValidator, youtube_validator])

    def __str__(self):
        return f'Lecture "{self.name}"'
