from django.urls import path
from .views import create_user, get_user, get_users

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/<int:id>/', get_user, name='get_user'),
    path('users/create/', create_user, name='create_user')
]