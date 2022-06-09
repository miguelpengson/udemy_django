from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=64, unique=True, default='name@email.com')

    def __str__(self):
        return self.first_name