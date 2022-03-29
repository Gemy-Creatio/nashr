from django.urls import path
from main.views import (
    HomepageView,
    WhopageView,
ServicesPageView,
FoundationPageView,
PersonalPageView ,
ErrorView
)

urlpatterns = [
    path('', HomepageView.as_view(), name='home-page'),
    path('whous', WhopageView.as_view(), name='whous-page'),
    path('services', ServicesPageView.as_view(), name='services-page'),
    path('member/foundation', FoundationPageView.as_view(), name='found-page'),
    path('member/peronal', PersonalPageView.as_view(), name='person-page'),
    path('error', ErrorView.as_view(), name='error-page'),

]
