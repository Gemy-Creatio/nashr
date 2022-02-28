from django.db import models
from ordered_model.models import OrderedModel
# Create your models here.
from accounts.models import (
    User
)


class TakeDesign(OrderedModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
    min_price = models.IntegerField(null=True, blank=True)
    max_price = models.IntegerField(null=True, blank=True)
    what_designer_introduce = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        pass
