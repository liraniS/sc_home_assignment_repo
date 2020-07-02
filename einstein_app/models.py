from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=320, null=True)
    category = models.ForeignKey('Category', blank=True, null=True, related_name='course_category', on_delete=models.SET_NULL)
    by_user = models.ForeignKey(User, blank=True, null=True, related_name='by_user', on_delete=models.SET_NULL)
    enrolled_users = models.ManyToManyField(User, blank=True, null=True, related_name='enrolled_users')
    creation_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=80)
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    topic = models.CharField(max_length=80)
    message = models.TextField(max_length=320, null=True, blank=True)
    time_sent = models.DateTimeField(auto_now_add=True)
    answer = models.TextField(max_length=320, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ': '
        + self.topic + ' ' + self.time_sent.strftime("%m/%d/%Y, %H:%M:%S")