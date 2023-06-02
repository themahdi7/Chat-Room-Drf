from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views
from .views import UserRegisterView, LogOutView

app_name = 'accounts'
urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='login'),
    path("refresh", TokenRefreshView.as_view(), name="refresh"),
    path('register', UserRegisterView.as_view(), name='login'),
    path('logout', LogOutView.as_view(), name='logout'),
    path('profile', views.UserView.as_view(), name='profile_view'),
]
