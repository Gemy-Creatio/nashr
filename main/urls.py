from django.urls import path
from main.views import (
    HomepageView,
WhoUsView,
AboutView
)

urlpatterns = [
    path('', HomepageView.as_view(), name='home-page'),
    path('whous', WhoUsView.as_view(), name='whous-page'),
    path('about', AboutView.as_view(), name='about-page'),

]
