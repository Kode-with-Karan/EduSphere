from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('change_profile/', views.change_profile, name='change_profile'),
    path('audio-library/', views.audio_library, name='audio_library'),
    path('video-library/', views.video_library, name='video_library'),
    path('articles-blogs/', views.articles_blogs, name='articles_blogs'),
    path('categories/', views.categories, name='categories'),
    path('latest-updates/', views.latest_updates, name='latest_updates'),
    path('community/', views.community, name='community'),
    path('faq/', views.faq, name='faq'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('downloads/', views.downloads, name='downloads'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'), 
    path('upload/<str:category1>/<str:category2>/', views.upload_file, name='upload_file'),
]
