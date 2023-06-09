from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
import os
from gtts import gTTS
from translate import Translator
import speech_recognition as sr
import time
from playsound import playsound
from .models import *
from .forms import FeedbackForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError


def registerpage(request):
    if request.method == 'POST':
        if request.POST.get('password1')==request.POST.get('password2'):
            try:
                saveuser = User.objects.create_user(request.POST.get('username'),password=request.POST.get('password1'))
                saveuser.save()
                return render(request,'register.html',{'form':UserCreationForm(),'info':' The user ' + request.POST.get('username')+ ' is saved successfully.'})
            except IntegrityError:
                return render(request,'register.html',{'form':UserCreationForm(),'error':'The user '+ request.POST.get('username')+' is already exists'})
        else:
            return render(request,'register.html',{'form':UserCreationForm(),'error':'The passwords are not matching.. '})

    else:
        return render(request,'register.html',{'form':UserCreationForm})


def loginpage(request):
    if request.method=='POST':
        loginsuccess=authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
        if loginsuccess is None:
            return render(request, 'login.html', {'form': AuthenticationForm(),  'error': ' The username and password are not matching '})
        else:
            login(request,loginsuccess)
            return redirect('home')
    else:
        return render(request, 'login.html', {'form': AuthenticationForm()})



def logoutpage(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')


"""

def register(request):
    form=RegistrationForm

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    context = {'form': form}
    return render(request, 'register.html',context)

def register(request):
    form=CreateUserForm
    context = {'form': form}
    return render(request, 'register.html',context)
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')





def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password1')
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/')


        #user= RegistrationForm(request,username=username,password=password)

        #if user is not None:
         #   login(request)
          #  redirect('/')

    return render(request,'login.html')


def logout(request):
    return redirect('login')
    
"""

def feedback(request,form=''):
    #form=FeedbackForm()
    if request.method=='POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()

    context={'form':FeedbackForm}
    return render(request,'feedback.html',context)


def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')





def text_text(request,data1='',lang=''):
    if request.method == "POST":
            #data1=None
            data = request.POST.get('name')
            #print(data)
            languages1 = request.POST.get('languages1')
            print(languages1)
            languages= request.POST.get('languages')
            print(languages)
            translator = Translator(from_lang=languages1,to_lang=languages)
            data1 = translator.translate(data)
            print(data1)

    return render(request, 'sample.html',{'data1':data1})

def text_speech(request,data2='',translation='',data=''):
    if request.method == "POST":
        data = request.POST.get('name1')
        languages1 = request.POST.get('languages1')
        print(languages1)
        languages = request.POST.get('languages')
        print(languages)
        translator = Translator(from_lang=languages1, to_lang=languages)
        translation = translator.translate(data)
        #print(translation)
        data2 = gTTS(text=translation)
        data2.save("voice.mp3")
        os.system("voice.mp3")
    return render(request, 'text_speech.html', {'data2': data2,'translation':translation,'data':data})

def speech_text(request,data3='',audio_data='',text=''):
        if request.method == "POST":
            r = sr.Recognizer()
            print("Please talk")
            with sr.Microphone() as source:
                # read the audio data from the default microphone
                audio_data = r.record(source, duration=10)
                print("Recognizing...")
                # convert speech to text
                text = r.recognize_google(audio_data)
                print("Recognised Speech:" + text)
                languages1 = request.POST.get('languages1')
                print(languages1)
                languages = request.POST.get('languages')
                print(languages)
                translator = Translator(from_lang=languages1, to_lang=languages)

                #translator = Translator(from_lang="english", to_lang="marathi")
                data3 = translator.translate(text)
                print(data3)
        return render(request, 'speech_text.html', {'audio_data':audio_data,'data3': data3,'text':text})



def speech_speech(request,data4='',audio_data='',text='',translation=''):
    try:
        if request.method == "POST":
            r = sr.Recognizer()
            print("Please talk")
            with sr.Microphone() as source:
                # read the audio data from the default microphone
                audio_data = r.record(source, duration=10)
                print("Recognizing...")
                # convert speech to text
                text = r.recognize_google(audio_data)
                print("Recognised Speech:" + text)
                languages1 = request.POST.get('languages1')
                print(languages1)
                languages = request.POST.get('languages')
                print(languages)
                translator = Translator(from_lang=languages1, to_lang=languages)

                #translator = Translator(from_lang="english", to_lang="marathi")
                translation = translator.translate(text)
                print(translation)
                data4 = gTTS(text=translation)
                data4.save("voice.mp3")
                os.system("voice.mp3")
        return render(request, 'speech_speech.html', {'audio_data':audio_data,'data4': data4,'translation':translation,'text':text})
    except StopIteration:
        return
