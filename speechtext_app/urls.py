
from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
   # path('', views.index, name='view'),
    path('home', views.home, name='home'),
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout', views.logoutpage, name='logout'),
    path('feedback/', views.feedback, name='feedback'),
    path('text_text/', views.text_text, name='text_text'),
    path('text_speech/', views.text_speech, name='text_speech'),
   # path('text_text/',views.text_text,name='text_text'),
  #  path('trans/', views.text_text, name='speech_text'),
    path('speech_speech/', views.speech_speech, name='speech_speech'),
    path('speech_text/', views.speech_text, name='speech_text'),
   # path('trans', views.trans, name='trans'),

]