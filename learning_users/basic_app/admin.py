from django.contrib import admin
from basic_app.models import UserProfileInfo

# So we can edit the models in the admin page
admin.site.register(UserProfileInfo)
