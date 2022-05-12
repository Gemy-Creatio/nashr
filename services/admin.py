# Register your models here.
from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from services.models import (
    PaidVoucher,
    RequestDesignService,
    Vouchers,
    TranslateService,
    Vouchers ,
    PaidVoucher,
    PersonWork ,
    ContactRequestServices ,
    RequestBook ,
    NegotiationRequests
)

@admin.register(NegotiationRequests)
class NegotiationRequestsAdmin(OrderedModelAdmin):
    list_display = ("__str__",)


@admin.register(RequestBook)
class RequestBookAdmin(OrderedModelAdmin):
    list_display = ("__str__",)


@admin.register(ContactRequestServices)
class ContactRequestServicesAdmin(OrderedModelAdmin):
    list_display = ("__str__",)


@admin.register(PersonWork)
class PersonWorkAdmin(OrderedModelAdmin):
    list_display = ("__str__",)

@admin.register(RequestDesignService)
class RequestDesignServiceAdmin(OrderedModelAdmin):
    list_display = ("__str__",)

@admin.register(TranslateService)
class TranslateServiceAdmin(OrderedModelAdmin):
    list_display = ("__str__",)


@admin.register(Vouchers)
class VouchersAdmin(OrderedModelAdmin):
    list_display = ("__str__",)
    
    

@admin.register(PaidVoucher)
class PaidVoucherAdmin(OrderedModelAdmin):
    list_display = ("__str__",)




