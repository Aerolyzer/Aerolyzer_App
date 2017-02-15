from django.http import HttpResponse
import datetime
from django.shortcuts import render
from app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
	
def index(request):
	return render(request, 'app/index.html')
	
def about(request):
	return render(request, 'app/about.html')
	
def faq(request):
	return render(request, 'app/faq.html')
	
@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('app/signup_complete')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'app/signup.html',
    variables,
    )
 
def signup_complete(request):
    return render_to_response(
    'app/signup_complete.html',
    )
 
def logout(request):
    logout(request)
    return HttpResponseRedirect('/')
 
# @login_required
# def gallery(request):
    # return render_to_response(
    # 'gallery.html',
    # { 'user': request.user }
    # )
