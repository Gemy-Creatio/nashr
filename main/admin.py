from django.contrib import admin
from solo.admin import SingletonModelAdmin
from ordered_model.admin import OrderedModelAdmin
from main.models import (
    WhoUS,
    TranslatorMembershipTerms,
    Privacy,
    Homepage,
PublishingBook,
    FAQ
)


# Register your models here.
@admin.register(FAQ)
class FAQAdmin(OrderedModelAdmin):
    list_display = ("__str__",)


@admin.register(Homepage)
class HomeAdmin(SingletonModelAdmin):
    list_display = ("__str__",)


@admin.register(WhoUS)
class WhoUSAdmin(SingletonModelAdmin):
    list_display = ("__str__",)


@admin.register(TranslatorMembershipTerms)
class MembershipTermsAdmin(SingletonModelAdmin):
    list_display = ("__str__",)


@admin.register(PublishingBook)
class PublishingBookAdmin(SingletonModelAdmin):
    list_display = ("__str__",)


@admin.register(Privacy)
class PrivacyAdmin(SingletonModelAdmin):
    list_display = ("__str__",)
