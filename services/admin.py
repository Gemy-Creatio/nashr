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
)


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




