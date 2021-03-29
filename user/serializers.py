from rest_framework.serializers import ModelSerializer
from user.models import User, WorkExperience


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class WorkExpSerializer(ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'
