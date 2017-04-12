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
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def index(request):
	if request.method == 'POST':
		usr = request.POST['username']
		psswd = request.POST['password']
		user = authenticate(username=usr, password=psswd)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('gallery')
		else:
			return render(request, 'app/index.html', {'login_message' :
				'That username/password doesn\'t work!'},)
	return render(request, 'app/index.html', {'user': request.user,
		'is_index':True},)

def about(request):
	return render(request, 'app/about.html', {'user': request.user},)

def faq(request):
	return render(request, 'app/faq.html', {'user': request.user},)

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
	{'form': form, 'user': request.user, 'is_index':True,},
	)

def signup_complete(request):
	return render(request, 'app/signup_complete.html',{ 'user': request.user },)

@login_required
def gallery(request):
    return render(request,
    'app/gallery.html',
	{ 'user': request.user },
    )

@login_required
def upload(request):
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		# verified = imgRestFuncs(filename)
		# if verified['is_verified']:
		# 	return render(request,
		# 	'app/upload.html',
		# 	{ 'user': request.user, 'file_name': filename, 'error_message' :
		# 		verified['msg']},)
		# else:
		# 	return render(request,
		# 	'app/retrieve.html',
		# 	{ 'user': request.user, 'file_name': filename },)
		return render(request,
		'app/upload.html',
		{ 'user': request.user, 'filename': filename,})
	return render(request, 'app/upload.html', { 'user': request.user },)

@login_required
def profile(request):
    return render(request,
    'app/profile.html',
	{ 'user': request.user },
    )

@login_required
def retrieve(request):
    return render(request,
    'app/retrieve.html',
	{ 'user': request.user },
    )

@login_required
def results(request):
    return render(request,
    'app/results.html',
	{ 'user': request.user },
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/app')
