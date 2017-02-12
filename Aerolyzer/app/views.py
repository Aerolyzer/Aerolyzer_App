from django.http import HttpResponse
import datetime
from django.shortcuts import render

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
	
def index(request):
	return render(request, 'app/index.html')
	
def about(request):
	return render(request, 'app/about.html')
	
def faq(request):
	return render(request, 'app/faq.html')