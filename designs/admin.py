from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from designs.models import (
TakeDesign
)
# Register your models here.


@admin.register(TakeDesign)
class UserProfileAdmin(OrderedModelAdmin):
    list_display = ("__str__",)
