from django.shortcuts import render

def index(request):
    my_dict = {'insert_content': "Helllo I am form firstapp views!"}
    return render(request, 'first_app/index.html', context=my_dict)
