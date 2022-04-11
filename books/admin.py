from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from books.models import (
    BookContract,
    Book,
    BookVoucher,
    ContractFollow,
    UserProfile,
    PublisherNeeds,
    BookDistrubuting,
    Negotiation,
    FoundtationUserProfile,
    AdvertisePresent,
    NeedsPresent ,
    CopyRightContract ,
    NegotiationBook ,


)

@admin.register(NegotiationBook)
class NegotiationBookAdmin(OrderedModelAdmin):
    list_display = ("__str__",)

@admin.register(CopyRightContract)
class CopyRightContractAdmin(OrderedModelAdmin):
    list_display = ("__str__",)


@admin.register(NeedsPresent)
class NeedsPresentAdmin(OrderedModelAdmin):
    list_display = ("__str__",)


@admin.register(AdvertisePresent)
class AdvertisePresentProfileAdmin(OrderedModelAdmin):
    list_display = ("__str__",)


@admin.register(FoundtationUserProfile)
class FoundtationUserProfileAdmin(OrderedModelAdmin):
    list_display = ("__str__",)


@admin.register(BookDistrubuting)
class BookDistrubutingAdmin(OrderedModelAdmin):
    list_display = ("__str__",)


@admin.register(Negotiation)
class NegotiationAdmin(OrderedModelAdmin):
    list_display = ("__str__",)


@admin.register(PublisherNeeds)
class PublisherNeedsAdmin(OrderedModelAdmin):
    list_display = ("__str__",)


@admin.register(UserProfile)
class UserProfileAdmin(OrderedModelAdmin):
    list_display = ("__str__",)


# Register your models here.
@admin.register(BookContract)
class BookContractAdmin(OrderedModelAdmin):
    list_display = ("__str__",)


@admin.register(Book)
class BookAdmin(OrderedModelAdmin):
    list_display = ("__str__",)


@admin.register(BookVoucher)
class BookVoucherAdmin(OrderedModelAdmin):
    list_display = ("__str__",)


@admin.register(ContractFollow)
class ContractFollowAdmin(OrderedModelAdmin):
    list_display = ("__str__",)
