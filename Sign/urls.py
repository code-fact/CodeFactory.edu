from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register.as_view(), name='register'),
    path('profile', views.profile.as_view(), name='profile'),
]
