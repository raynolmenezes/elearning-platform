from attr import fields
from django import forms
from django.contrib.auth.models import User
from users.models import UserProfileInfo
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta():
        model=User
        fields={'username','first_name','last_name','email','password','passwordv'}

        labels={
            'password':"Password",
            'passwordv':"Confirm Password"
        }

class UserProfileIntoForm(forms.ModelForm):
    teacher = 'teacher'
    student = 'student'

    user_types = [
        (teacher, 'teacher'),
        (student, 'student'),
    ]

    user_type = forms.ChoiceField(required=True, choices=user_types)

    class Meta():
        model= UserProfileInfo
        fields={'profile_pic','user_type'}
