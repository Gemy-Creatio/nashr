from django.urls import path
from .views import (
    logoutUser,
    LoginView,
    RegisterView,
)

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', logoutUser, name='logout'),

]
