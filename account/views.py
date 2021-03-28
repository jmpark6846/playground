from rest_framework.viewsets import ModelViewSet
from account.models import User
from account.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
