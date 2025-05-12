from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'list-adms', ListAdmsViewSet, basename='list_adms')
router.register(r'list-professors', ListProfessorsViewSet, basename='list_professors')
router.register(r'meeting', MeetingViewSet)
router.register(r'meeting-professor', MeetingProfessorViewSet, basename='meeting_professor')
router.register(r'classroom', ClassroomViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomAuthToken.as_view(), name='login_user'),
    path('register-adm/', RegisterAdmView.as_view(), name='register_adm'),
    path('register-prof/', RegisterProfessorView.as_view(), name='register_prof'),
]