"""urls module"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account.application.views.user_view import UserView

ROUTER = DefaultRouter()
ROUTER.register(r'users', UserView, basename='api_account_users')

urlpatterns = [
    path('', include(ROUTER.urls)),
]
