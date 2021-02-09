from rest_framework import serializers
from user.models import User, ActivityPeriod

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = User
        fields = "__all__"

class ActivityPeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = ActivityPeriod
        fields = "__all__"
