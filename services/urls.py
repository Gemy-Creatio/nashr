from django.urls import path
from services.views import (
    RequestTranslateServiceView,
    RequestDesignServiceView,
    AllServicesForDesignView,
    CreateTakeDesignRequest,
    RequestServiceDetails,
    AllVouchers,
    PayVoucher,
    TranslationRequestView,
    RequestSubtitleServiceView,
    HomeTranslationRequestView,
    AllMessagesView,
    AllBooksForTranslatorView , 
    PersonalContractChoices ,
    AllBookContractsForUser ,
    AllCopyContractsForUser ,
    AcceptBookContract ,
    AcceptCopyrightContract,
    AllWorks,
)

urlpatterns = [
    path('all/works', AllWorks,
         name='all-works'),
    path('request/translate', RequestTranslateServiceView.as_view(),
         name='request-translate'),
    path('request/design', RequestDesignServiceView.as_view(), name='request-design'),
    path('request/subtitle', RequestSubtitleServiceView.as_view(),
         name='request-subtitle'),
    path('all/designs', AllServicesForDesignView.as_view(), name='all-designs'),
    path('add/design', CreateTakeDesignRequest.as_view(), name='take-design'),
    path('design/details/<int:pk>',
         RequestServiceDetails.as_view(), name='detail-design'),
    path('all/vouchers', AllVouchers, name='all-vouchers'),
    path('all/vouchers/<int:pk>', PayVoucher, name='pay-voucher'),
    path('add/book/translate/<int:pk>',
         TranslationRequestView.as_view(), name='complete-book'),
    path('add/translate/home',
         HomeTranslationRequestView.as_view(), name='home-advertise'),
    path('all/msgs/home',
         AllMessagesView.as_view(), name='all-msg'),
     path('all/books/translator',
         AllBooksForTranslatorView.as_view(), name='all-books-trans'),
     path('contract/choices',
         PersonalContractChoices.as_view(), name='person-contract-choices'),
     path('all/copy/contract',
         AllCopyContractsForUser.as_view(), name='all-copycontract-user'),
     path('all/books/contracs',
         AllBookContractsForUser.as_view(), name='all-bookcontract-user'),
      path('accept/copy-contract/<int:pk>',
         AcceptCopyrightContract.as_view(), name='accept-copy'),
      path('accept/book-contract/<int:pk>',
         AcceptBookContract.as_view(), name='accept-book'),
]
