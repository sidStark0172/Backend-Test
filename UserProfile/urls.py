from django.urls import path
from .views import *

urlpatterns = [
    path('',activity.as_view(),name='activity')
]