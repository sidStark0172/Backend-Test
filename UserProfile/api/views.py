from datetime import datetime
from user.api.serializers import UserSerializer, ActivityPeriodSerializer
from user.models import User, ActivityPeriod
from django.conf import settings

from django.http import HttpResponseServerError,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets


@api_view(['GET'])
def get_users(request):
    try:

        all_users = User.objects.all()

        res = {
            "ok" : True,
        }

        user_list = []
        for u in all_users:
            temp = {
                'id' : u.id,
                'real_name' : u.real_name,
                'tz' : str(u.tz)
            }

            user_activities = ActivityPeriod.objects.filter(user=u)

            activities = []

            for a in user_activities:
                temp2 = {
                    'start_time'    : a.start_time.strftime("%b %d %Y  %I:%M%p"),
                    'end_time'      : a.end_time.strftime("%b %d %Y  %I:%M%p"),
                }

                activities.append(temp2)
            
            temp['activities'] = activities
            user_list.append(temp)

        res["members"] = user_list

        return Response(res)
    
    except Exception as e:
        print(e)
        response_data = {}
        response_data['message'] = "Some error occured"
        return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
