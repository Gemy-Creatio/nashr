from django.contrib import admin
from solo.admin import SingletonModelAdmin
from main.models import (
    About,
    WhoUS,
    MembershipTerms,
    Privacy,
    Homepage
)


# Register your models here.


@admin.register(About)
class AboutAdmin(SingletonModelAdmin):
    list_display = ("__str__",)


@admin.register(Homepage)
class HomeAdmin(SingletonModelAdmin):
    list_display = ("__str__",)


@admin.register(WhoUS)
class WhoUSAdmin(SingletonModelAdmin):
    list_display = ("__str__",)


@admin.register(MembershipTerms)
class MembershipTermsAdmin(SingletonModelAdmin):
    list_display = ("__str__",)


@admin.register(Privacy)
class PrivacyAdmin(SingletonModelAdmin):
    list_display = ("__str__",)
