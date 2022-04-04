from django.urls import path
from designs.views import (
    CreateFormationRequestView,
    CreatePrintRequestView,
    AllPrintRequestView,
    TranslatorServicesView , 
    DesignerServicesView
)

urlpatterns = [
    path('request/print', CreatePrintRequestView.as_view(), name='print-request'),
    path('all/prints', AllPrintRequestView.as_view(), name='all-prints'),
    path('create/formation/request', CreateFormationRequestView.as_view(), name='book-format'),
    path('translator/terms', TranslatorServicesView.as_view(), name='translator-terms')
    path('designer/terms', DesignerServicesView.as_view(), name='designer-terms')

]
