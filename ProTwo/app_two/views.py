from django.shortcuts import render
from .forms import NewUserForm

def index(request):
    return render(request, 'app_two/index.html',)

def help(request):
    help_dict = { 'help_me': 'Please help me I do not know what I am doing!' }
    return render(request, 'app_two/help.html', context=help_dict)

def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('Error form is invalid!')

    return render(request, 'app_two/users.html', {'form': form})



