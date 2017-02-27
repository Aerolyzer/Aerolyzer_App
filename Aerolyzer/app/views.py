from django.http import HttpResponse
import datetime
from django.shortcuts import render
from app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
	
def index(request):
	return render(request, 'app/index.html')
	
def about(request):
	return render(request, 'app/about.html')
	
def faq(request):
	return render(request, 'app/faq.html')
	
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return render(request,
            'app/signup_complete.html',
	RequestContext(request)
    )
    else:
        form = RegistrationForm()
 
    return render(request,
    'app/signup.html',
    {'form': form,},
    )
 
def signup_complete(request):
    return render(request,
    'app/signup_complete.html',
    )

def gallery(request):
    return render(request,
    'app/gallery.html',
    )
	
def upload(request):
    return render(request,
    'app/upload.html',
    )
	
def profile(request):
    return render(request,
    'app/profile.html',
    )
 
def logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# TODO when database is setup	
# @login_required
# def gallery(request):
    # return render_to_response(
    # 'gallery.html',
    # { 'user': request.user }
    # )
	
	
