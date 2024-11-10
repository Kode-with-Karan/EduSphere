from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('audio-library/', views.audio_library, name='audio_library'),
    path('video-library/', views.video_library, name='video_library'),
    path('articles-blogs/', views.articles_blogs, name='articles_blogs'),
    path('categories/', views.categories, name='categories'),
    path('latest-updates/', views.latest_updates, name='latest_updates'),
    path('subscription/', views.subscription, name='subscription'),
    path('community/', views.community, name='community'),
    path('faq/', views.faq, name='faq'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('downloads/', views.downloads, name='downloads'),
]
