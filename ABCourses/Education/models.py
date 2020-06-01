from django.db import models


class BaseUser(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True)
    user_name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return f'User {self.user_name}'


class Teacher(models.Model):
    base_id = models.ForeignKey('BaseUser', on_delete=models.CASCADE)


class Student(models.Model):
    base_id = models.ForeignKey('BaseUser', on_delete=models.CASCADE)


class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    # rating = models.FloatField
    BEGINER = 'B'
    INTERMEDIATE = 'I'
    ADVANCED = 'A'
    LEVELS = [
        (BEGINER, 'Beginer'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced')
    ]
    level = models.CharField(max_length=255, choices=LEVELS, default=BEGINER)


class Lecture(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
