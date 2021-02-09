from django.urls import path, include
from django.conf import settings
from UserProfile.api import views
from rest_framework import routers


urlpatterns = [
    path('get/', views.get),
]
