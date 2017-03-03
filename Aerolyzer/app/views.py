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
from django.contrib.auth import authenticate, login

#TODO add login authentication to every page
def index(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('gallery')
		else:
			return HttpResponseRedirect('faq')
	return render(request, 'app/index.html', {'user': request.user},)

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
			email=form.cleaned_data['email'],
			password=form.cleaned_data['password1']
			)
			return HttpResponseRedirect('signup_complete')
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

@login_required
def gallery(request):
    return render(request,
    'app/gallery.html',
	{ 'user': request.user },
    )

@login_required
def upload(request):
    return render(request,
    'app/upload.html',
	{ 'user': request.user },
    )

@login_required
def profile(request):
    return render(request,
    'app/profile.html',
	{ 'user': request.user },
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/app')
