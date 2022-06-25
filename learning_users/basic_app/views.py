from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm

def index(request):
    return render(request, 'basic_app/index.html')


def register(request):
    registered = False
    if request.method == "POST":
        # Grab information from the userform and profileform
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check if the forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            # Hashing the password by using the set_password method
            user.set_password(user.password)
            user.save()
            # Get errors with collisions where it tries to overide user
            profile = profile_form.save(commit=False)
            # One to one from models is defined here
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()


    return render(request, 'basic_app/registeration.html',{
        'user_form':user_form, 'profile_form':profile_form, 'registered':registered})