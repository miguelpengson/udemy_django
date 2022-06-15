from django.shortcuts import render

def index(request):


    return render(request, 'basic_app/index.html')


def register(request):
    registered = False
    if request.method == "POST":
        user_form
    return render(request, 'basic_app/register.html')