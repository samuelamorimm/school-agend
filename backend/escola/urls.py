from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='login_user'),
    path('register-adm/', RegisterAdmView.as_view(), name='register_adm'),
    path('register-prof/', RegisterProfessorView.as_view(), name='register_prof'),
]