from django.shortcuts import render
from . import forms

def index(request):
    return render(request, 'basic_app/index.html')

def form_name_view(request):
    form = forms.FormName()
    if request.method =='POST':
        



    return render(request, 'basic_app/form_page.html', {'form':form})
     
