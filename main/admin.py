from django.contrib import admin

# Register your models here.
from .models import UserProfile,MediaUpload

# Register the UserProfile model
admin.site.register(UserProfile)
admin.site.register(MediaUpload)