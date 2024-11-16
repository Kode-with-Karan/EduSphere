# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile
from .models import Thread, Post

from .models import MediaUpload

class MediaUploadForm(forms.ModelForm):
    class Meta:
        model = MediaUpload
        fields = ['category', 'name', 'description', 'audio_file', 'text_file', 'video_file']

class UserProfileForm(forms.ModelForm):
    full_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = ['full_name', 'mobile', 'address', 'website', 'github', 'twitter', 'instagram', 'facebook']

    def __init__(self, *args, **kwargs):
        # Get the user instance from the view
        user = kwargs.pop('user', None)
        super(UserProfileForm, self).__init__(*args, **kwargs)
        
        # Populate initial data for the user fields
        if user:
            self.fields['full_name'].initial = user.get_full_name()
            self.fields['email'].initial = user.email

            # Populate initial data for the UserProfile fields if available
            if hasattr(user, 'userprofile'):
                profile = user.userprofile
                self.fields['mobile'].initial = profile.mobile
                self.fields['address'].initial = profile.address
                self.fields['website'].initial = profile.website
                self.fields['github'].initial = profile.github
                self.fields['twitter'].initial = profile.twitter
                self.fields['instagram'].initial = profile.instagram
                self.fields['facebook'].initial = profile.facebook

    def save(self, commit=True):
        # Save user-related fields
        profile = super(UserProfileForm, self).save(commit=False)
        profile.user.email = self.cleaned_data['email']
        
        # Split full_name into first and last names
        full_name = self.cleaned_data['full_name']
        profile.user.first_name = full_name.split(' ')[0] if full_name else ''
        profile.user.last_name = ' '.join(full_name.split(' ')[1:]) if full_name else ''
        
        if commit:
            profile.user.save()
            profile.save()
        return profile
    
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords don't match")
        return password_confirm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput)




class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Write your Title here...',
                # 'class': 'form-control',  # Optional: Add additional CSS classes
                # 'rows': 4,                # Optional: Control the height of the textarea
            }),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your comment here...',
                # 'class': 'form-control',  # Optional: Add additional CSS classes
                # 'rows': 4,                # Optional: Control the height of the textarea
            }),
        }
