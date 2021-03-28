from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from account.models import User
from account.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
