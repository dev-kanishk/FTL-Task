
from rest_framework import  serializers
from .models import User,activity_period


class ActivityPeriodSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format='%b %e %Y %l:%M %p')
    end_time = serializers.DateTimeField(format='%b %e %Y %l:%M %p')

    class Meta:
        model = activity_period
        fields = ['start_time', 'end_time']

class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'real_name', 'tz', 'activity_periods']


class testSerializer(serializers.Serializer):
    ok = serializers.SerializerMethodField('get_true')
    members = serializers.SerializerMethodField('get_members')
    

    def __init__(self,users):
        self.users = users
        super(testSerializer, self).__init__(users)
        
        

    def get_members(self, *args):
        
        return UserSerializer(
                    self.users,
                    many=True
                ).data

    def get_true(self, *args):
        return True