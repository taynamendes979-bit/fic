from django import forms
from .models import Area, Publico, Curso
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm 
    class Meta:
        model = UserCreationForm 
        fealds = [ 
            'cpf',
            'nascimento',
            'usernamer',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
            ]
class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome']