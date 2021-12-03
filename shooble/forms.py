from django import forms
from django.contrib.auth.models import User
from .models import ProfilePic


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        # widgets = {
        #     'first_name': forms.TextInput(attrs={
        #         'class': 'requiredField',
        #     }),
        #     'last_name': forms.TextInput(attrs={
        #         'class': 'requiredField',
        #     }),
        #     'email': forms.EmailInput(attrs={
        #         'class': 'requiredField',
        #     }),
        # }


class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = ProfilePic
        fields = ['profile_pic']
