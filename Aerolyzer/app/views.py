from django.http import HttpResponse
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
		uploadedFileUrl = fs.url(filename)
		request.session['filename'] = filename
		request.session['uploadedFileUrl'] = uploadedFileUrl
		# verified = imgRestFuncs(filename)
		# if not verified['isVerified']:
		# 	return render(request,
		# 	'app/upload.html',
		# 	{ 'user': request.user, 'filename': filename, 'uploadedFileUrl': uploadedFileUrl,
		# 	'error_message': verified['data']},)
		# else:
		#	request.session['exifData'] = verified['data']
		return HttpResponseRedirect('retrieve')
	return render(request, 'app/upload.html', { 'user': request.user, },)

@login_required
def profile(request):
    return render(request,
    'app/profile.html',
	{ 'user': request.user, },
    )

@login_required
def retrieve(request):
	uploadedFileUrl = request.session['uploadedFileUrl']
	filename = request.session['filename']
	# exifData = request.session['exifData']

	if request.method == 'POST':
		# wunderData = retrieve_weather_info(exifData['location'])
		# if wunderData is None:
		# 	return render(request,
		#     'app/retrieve.html',
		# 	{ 'user': request.user, 'error_message': 'weather' },
		#     )
		# request.session['wunderData'] = wunderData
		# misrData = retrieve_misr_info(exifData['location'])
		# if misrData is None:
		# 	return render(request,
		#     'app/retrieve.html',
		# 	{ 'user': request.user, 'error_message': 'satellite' },
		#     )
		# request.session['misrData'] = misrData
	    # return render(request,
	    # 'app/retrieve.html',
		# { 'user': request.user, 'exifData' : exifData,
		# 'wunderData': wunderData, 'misrData': misrData, 'all_clear': True, },
	    # )
	    return render(request,
	    'app/retrieve.html',
		{ 'user': request.user, 'exifData' : 'exif here',
		'wunderData': 'wunder here', 'misrData': 'misr here', 'all_clear': True,
		'filename': filename, 'uploadedFileUrl': uploadedFileUrl,},
	    )

	return render(request,
    'app/retrieve.html',
	{ 'user': request.user, 'filename': filename, 'uploadedFileUrl': uploadedFileUrl,
	'all_clear': False,},
    )

@login_required
def results(request):
	uploadedFileUrl = request.session['uploadedFileUrl']
	filename = request.session['filename']
	# exifData = request.session['exifData']
	# wunderData = request.session['wunderData']
	# misrData = request.session['misrData']
	# aerosol = coreAlgorithmHere(exifData, wunderData, misrData)
	# TODO use pysolr to add all to database
    # return render(request,
    # 'app/results.html',
	# { 'user': request.user, 'aerosol': aerosol,
	# 'filename': filename, 'uploadedFileUrl': uploadedFileUrl,},
    # )
	return render(request,
    'app/results.html',
	{ 'user': request.user, 'filename': filename, 'uploadedFileUrl': uploadedFileUrl,},
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/app')
