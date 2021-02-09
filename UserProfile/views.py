from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.contrib.auth.models import User

#All user activity tracking api
class activity(APIView):
    def get(self, request):
        user_list = User.objects.all()
        members = []
        for item in user_list:
            id = item.username
            real_name = item.first_name + ' ' + item.last_name
            tz = item.profile.time_zone
            activity_periods = Activity.objects.filter(user = item).values('start_time','end_time')
            members.append({
                "id" : id,
                "real_name" : real_name,
                "tz" : tz,
                "activity_periods" : activity_periods
            })

        return Response({'ok':True,'members':members}, status=status.HTTP_201_CREATED)