from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=[('student', 'Student'), ('teacher', 'Teacher')], required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']