from django.db import models


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
