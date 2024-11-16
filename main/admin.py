from django.contrib import admin

# Register your models here.
from .models import UserProfile,MediaUpload,Thread,Category,Post

# Register the UserProfile model
admin.site.register(UserProfile)
admin.site.register(MediaUpload)
admin.site.register(Thread)
admin.site.register(Category)
admin.site.register(Post)