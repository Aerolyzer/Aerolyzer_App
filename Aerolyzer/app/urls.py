from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^about$', views.about, name='about'),
	url(r'^faq$', views.faq, name='faq'),
	# Signup URLs
    url(r'^signup$', views.signup, name='signup'),
    url(r'^signup_complete$', views.signup_complete, name='signup_complete'),

]
