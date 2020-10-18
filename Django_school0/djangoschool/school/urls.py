from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from school.views import *


#ดึงฟังชั่น HomePage มาทำงาน

urlpatterns = [
	# localhost:8000/
	path('',HomePage, name='home-page'),
	path('about/', AboutPage, name='about-page'),
	path('contact/', ContactUs, name='contact-page'),
	path('score/', ShowScore, name='score-page'),
	path('register/', Register, name='register-page'),
	path('search/', SearchStudent, name='search-page'),
	path('profile/',EditProfile, name='edit-profile'),
	path('document/',ShowDocument,name='document-page')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
