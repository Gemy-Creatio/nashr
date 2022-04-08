from django.urls import path
from designs.views import (
    CreateFormationRequestView,
    CreatePrintRequestView,
    AllPrintRequestView,
    TranslatorServicesView , 
    DesignerServicesView , 
    PrinterServiceView ,
    ProofWriterTerms,
    BookAdvertiseTerms ,
    BookFormatTerms,
    CopyrightsTerms ,
    DesignCoverTerms ,
    PrinterRequestTerms

)

urlpatterns = [
    path('request/print', CreatePrintRequestView.as_view(), name='print-request'),
    path('all/prints', AllPrintRequestView.as_view(), name='all-prints'),
    path('create/formation/request', CreateFormationRequestView.as_view(), name='book-format'),
    path('translator/terms', TranslatorServicesView.as_view(), name='translator-terms') ,
    path('designer/terms', DesignerServicesView.as_view(), name='designer-terms'),
    path('printer/terms', PrinterServiceView.as_view(), name='printer-terms') ,
    path('proof-writer/terms', ProofWriterTerms.as_view(), name='proof_writer-terms') ,
    path('book-advertise/terms', BookAdvertiseTerms.as_view(), name='book-advertise-terms') ,
    path('book-format/terms', BookFormatTerms.as_view(), name='book-format-terms') ,
    path('book-advertise/terms', BookAdvertiseTerms.as_view(), name='book-advertise-terms') ,
    path('copy-rights/terms', CopyrightsTerms.as_view(), name='copyrights-terms') ,
    path('design-cover/terms', DesignCoverTerms.as_view(), name='design-cover-terms') ,
    path('printer-request/terms', PrinterRequestTerms.as_view(), name='printer-request-terms') ,


]
