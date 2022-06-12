from django import forms
from .models import User

class NewUserForm(forms.ModelForm):
    class Meta():
        # From the models.py file 
        model = User
        fields = '__all__'