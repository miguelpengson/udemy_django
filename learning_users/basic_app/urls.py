from django.urls import path
from . import views

# Template Urls in the html files ex {%url, 'index' %} -set up the app_name
app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register, name='register'),
]