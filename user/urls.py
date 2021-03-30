from django.urls import path, include
from user.views import UserViewSet, UserRegisterView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls

urlpatterns += [
    path('registration/', UserRegisterView.as_view(), name='registration'),

]
