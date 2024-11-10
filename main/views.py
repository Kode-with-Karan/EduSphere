from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about_us(request):
    return render(request, 'main/about_us.html')

def audio_library(request):
    return render(request, 'main/audio_library.html')

def video_library(request):
    return render(request, 'main/video_library.html')

def articles_blogs(request):
    return render(request, 'main/articles_blogs.html')

def categories(request):
    return render(request, 'main/categories.html')

def latest_updates(request):
    return render(request, 'main/latest_updates.html')

def subscription(request):
    return render(request, 'main/subscription.html')

def community(request):
    return render(request, 'main/community.html')

def faq(request):
    return render(request, 'main/faq.html')

def contact_us(request):
    return render(request, 'main/contact_us.html')

def downloads(request):
    return render(request, 'main/downloads.html')
