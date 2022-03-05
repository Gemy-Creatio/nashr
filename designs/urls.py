from django.urls import path
from designs.views import (
    CreatePrintRequestView
)

urlpatterns = [
    path('request/print', CreatePrintRequestView.as_view(), name='print-request')
]
