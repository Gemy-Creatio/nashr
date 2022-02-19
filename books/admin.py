from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from books.models import (
    BookContract,
    Book,
    BookVoucher,
    ContractFollow,
    UserProfile,

)


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
