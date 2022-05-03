from django.db import models
from django.contrib.auth.models import User
import os

def path_and_rename(instance,filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]
    if instance.user.username:
        filename = 'pfp/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to,filename)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Picture", blank=True)

    teacher = 'teacher'
    student = 'student'

    user_types = [
        (teacher, 'teacher'),
        (student, 'student'),
    ]

    user_type = models.CharField(max_length=10, choices=user_types, default=student)


    def __str__(self):
        return self.user.username