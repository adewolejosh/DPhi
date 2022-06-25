from django.db import models
from django.contrib.auth.models import User


class Courses(models.Model):
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return '%s - %s' % (self.owner, self.name)


class CourseEnrolment(models.Model):
    course = models.ForeignKey(Courses, related_name='lessons', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='enrollers', symmetrical=False)

    def __str__(self):
        return 'List of enrols for %s' % self.course
