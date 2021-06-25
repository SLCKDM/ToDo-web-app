from django.forms import ModelForm
from .models import Todo, Profile
from django.contrib.auth.models import User
from django import forms


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()