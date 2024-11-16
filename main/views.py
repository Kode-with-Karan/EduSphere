from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile,MediaUpload
from .forms import UserProfileForm
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .forms import MediaUploadForm
from django.core.paginator import Paginator
from .models import Category, Thread, Post
from .forms import ThreadForm, PostForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'forum/category_list.html', {'categories': categories})

def thread_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    threads = category.threads.all()
    return render(request, 'forum/thread_list.html', {'category': category, 'threads': threads})

def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    posts = thread.posts.all()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.created_by = request.user
            post.save()
            return redirect('thread_detail', thread_id=thread_id)
    else:
        form = PostForm()

    return render(request, 'forum/thread_detail.html', {'thread': thread, 'posts': posts, 'form': form})

def create_thread(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES)  # Handle file uploads
        print(request.FILES)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.category = category
            thread.created_by = request.user
            thread.save()
            return redirect('thread_list', category_id=category.id)
    else:
        form = ThreadForm()

    return render(request, 'forum/create_thread.html', {'category': category, 'form': form})



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page or a different URL
    else:
        form = RegisterForm()
    return render(request, 'main/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page or a different URL
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logging out



def home(request):
    return render(request, 'main/home.html')

@login_required
def profile(request):
    user = request.user 
    profile = UserProfile.objects.get(user=user)
    return render(request, 'main/profile.html', {'user': user, 'profile': profile})

@login_required
def change_profile(request):

    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        # Initialize form with existing data
        form = UserProfileForm(
            instance=profile,
            initial={
                'full_name': f"{request.user.username}",
                'email': request.user.email,
            }
        )
        # form = UserProfileForm(instance=profile, user=request.user)
    return render(request, 'main/change_profile.html', {'form': form})

def audio_library(request):
    media = MediaUpload.objects.all()
    return render(request, 'main/audio_library.html', {'medias':media})

def video_library(request):
    media = MediaUpload.objects.all()
    return render(request, 'main/video_library.html',{'medias':media})

def articles_blogs(request):
    media_list = MediaUpload.objects.all()  # Get all media items
    paginator = Paginator(media_list, 10)  # Show 10 items per page

    # Get the page number from the request GET parameters (defaults to 1 if not provided)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number) 
    return render(request, 'main/articles_blogs.html', {'medias': page_obj})

def categories(request):
    return render(request, 'main/categories.html')

def latest_updates(request):
    return render(request, 'main/latest_updates.html')

def community(request):
    return render(request, 'main/community.html')

def faq(request):
    return render(request, 'main/faq.html')

def contact_us(request):
    return render(request, 'main/contact_us.html')

def downloads(request):
    return render(request, 'main/downloads.html')

def upload_file(request, category1, category2):

    if(category1 == 'ent'):
        cat = 'entertainment'
    elif(category1 == 'info'):
        cat = 'infotainment'
    else:
        cat = 'education' 

    if request.method == 'POST':
        form = MediaUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the uploaded files and other data
            return redirect('upload_file',category1=category1, category2=category2)  # Redirect to a success page or another view
    else:
        form = MediaUploadForm(
            initial={
                'category': f"{cat}",
                }
            
        )
    return render(request, 'main/uploadFiles.html', {'form': form, 'file_type':category2})

    