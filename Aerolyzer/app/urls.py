from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^about$', views.about, name='about'),
	url(r'^faq$', views.faq, name='faq'),
	# Signup URLs
    url(r'^signup$', views.signup, name='signup'),
    url(r'^signup_complete$', views.signup_complete, name='signup_complete'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^retrieve$', views.retrieve, name='retrieve'),
    url(r'^results$', views.results, name='results'),
    url(r'^logout_page/$', views.logout_page, name='logout_page'),
]
