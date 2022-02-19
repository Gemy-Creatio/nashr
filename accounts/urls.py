from django.urls import path
from .views import (
    logoutUser,
    LoginView,
    RegisterView,
UserDetails,
)

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', logoutUser, name='logout'),
    path('details/<int:pk>', UserDetails.as_view(), name='user-details'),

]
