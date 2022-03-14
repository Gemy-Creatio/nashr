from django.urls import path
from services.views import (
    RequestTranslateServiceView,
    RequestDesignServiceView,
    AllServicesForDesignView,
    CreateTakeDesignRequest,
    RequestServiceDetails , 
    AllVouchers,
    PayVoucher ,
    TranslationRequestView
)

urlpatterns = [
    path('request/translate', RequestTranslateServiceView.as_view(), name='request-translate'),
    path('request/design', RequestDesignServiceView.as_view(), name='request-design'),
    path('all/designs', AllServicesForDesignView.as_view(), name='all-designs'),
    path('add/design', CreateTakeDesignRequest.as_view(), name='take-design'),
    path('design/details/<int:pk>', RequestServiceDetails.as_view(), name='detail-design'),
    path('all/vouchers', AllVouchers, name='all-vouchers'),
    path('all/vouchers/<int:pk>', PayVoucher, name='pay-voucher'),
    path('add/book/translate/<int:pk>', TranslationRequestView.as_view(), name='complete-book'),

]
