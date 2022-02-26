from django.urls import path
from services.views import (
    RequestTranslateServiceView,
    RequestDesignServiceView,
    AllServicesForDesignView
)

urlpatterns = [
    path('request/translate', RequestTranslateServiceView.as_view(), name='request-translate'),
    path('request/design', RequestDesignServiceView.as_view(), name='request-design'),
    path('all/designs', AllServicesForDesignView.as_view(), name='all-designs')

]
