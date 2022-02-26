# Register your models here.
from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from services.models import (
    RequestDesignService,
    TranslateService
)


@admin.register(RequestDesignService)
class RequestDesignServiceAdmin(OrderedModelAdmin):
    list_display = ("__str__",)


@admin.register(TranslateService)
class TranslateServiceAdmin(OrderedModelAdmin):
    list_display = ("__str__",)
