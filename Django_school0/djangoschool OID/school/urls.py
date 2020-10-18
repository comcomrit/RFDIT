from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage, name='home-page'),
    path('about/', AboutPage, name='about-page'),
    path('contactus/', ContactUs, name='contact-page'),
    path('score/', ShowScore, name='score-page'),
    path('register/', Register, name='register-page')

]