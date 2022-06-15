from django.urls import path
from . import views

# Template Urls
app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register, name='register'),
]