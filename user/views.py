from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_auth.registration.views import RegisterView
from user.models import User, UserProfile, WorkExperience
from user.serializers import UserSerializer, WorkExpSerializer


class UserRegisterView(RegisterView):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # email = response.data['user']['email']
        # user = User.objects.get(email=email)
        # UserProfile.objects.create(
        #     user=user
        # )
        return response


class WorkExperienceViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkExpSerializer
    queryset = WorkExperience.objects.all()

    def list(self, request: Request, *args, **kwargs):
        queryset = self.queryset.filter(
            profile=request.user.profile
        )
        serializer = WorkExpSerializer(queryset, many=True)
        return Response(serializer.data)


class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
