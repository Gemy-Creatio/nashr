from django.urls import path
from designs.views import (
    CreatePrintRequestView,
    AllPrintRequestView
)

urlpatterns = [
    path('request/print', CreatePrintRequestView.as_view(), name='print-request')
    path('all/prints', AllPrintRequestView.as_view(), name='all-prints')

]
