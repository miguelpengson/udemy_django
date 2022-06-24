from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    # Allows us to extend the built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional aside from built in User model
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username