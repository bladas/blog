from django.urls import path

from home.views import Home, Contact, PostDescriptionView, About

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('contact/',Contact.as_view(),name='contact'),
    path('about-me/',About.as_view(),name='about'),
    path('<str:slug>/',PostDescriptionView.as_view(),name='post-decription')
]
