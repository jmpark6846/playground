from django.urls import path, include
from user.views import UserViewSet, UserRegisterView, WorkExperienceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'work_exps', WorkExperienceViewSet, basename='work_exp')

urlpatterns = router.urls

urlpatterns += [
    path('registration/', UserRegisterView.as_view(), name='registration'),

]
