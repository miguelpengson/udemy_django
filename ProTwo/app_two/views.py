from django.shortcuts import render
from app_two.models import User

def index(request):
    return render(request, 'app_two/index.html',)

def help(request):
    help_dict = { 'help_me': 'Please help me I do not know what I am doing!' }
    return render(request, 'app_two/help.html', context=help_dict)

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request, 'app_two/users.html', context=user_dict)