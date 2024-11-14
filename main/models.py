# models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)
    mobile = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    website = models.URLField(max_length=200, blank=True)
    github = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

CATEGORY_CHOICES = [
    ('infotainment', 'Infotainment'),
    ('entertainment', 'Entertainment'),
    ('education', 'Education'),
]

class MediaUpload(models.Model):
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=255)
    description = models.TextField()
    audio_file = models.FileField(upload_to='uploads/audio/', null=True, blank=True)
    text_file = models.FileField(upload_to='uploads/text/', null=True, blank=True)
    video_file = models.FileField(upload_to='uploads/video/', null=True, blank=True)

    def __str__(self):
        return self.name