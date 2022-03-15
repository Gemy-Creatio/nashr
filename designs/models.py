from django.db import models
from ordered_model.models import OrderedModel
# Create your models here.
from accounts.models import (
    User
)
from books.models import (
    Book
)


class TakeDesign(OrderedModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    min_price = models.IntegerField(null=True, blank=True)
    max_price = models.IntegerField(null=True, blank=True)
    what_designer_introduce = models.CharField(
        max_length=255, null=True, blank=True)

    class Meta:
        pass


class PrintBookRequest(OrderedModel):
    PAPER_SIZE = (
        ('A5', 'A5'),
        ('A4', 'A4'),
    )
    paper_size = models.CharField(
        max_length=255, null=True, blank=True, choices=PAPER_SIZE)
    PAPER_TYPE = (
        ('عادى', 'عادى'),
        ('لماع', 'لماع'),
        ('لاصق', 'لاصق'),
        ('مقوى', 'مقوى'),
    )
    paper_type = models.CharField(
        max_length=255, null=True, blank=True, choices=PAPER_TYPE)
    PRINT_COLOR = (
        ('أسود', 'أسود'),
        ('ملون', 'ملون'),
    )
    print_color = models.CharField(
        max_length=255, null=True, blank=True, choices=PRINT_COLOR)
    PRINT_FACES = (
        ('وجه واحد', 'وجة واحد'),
        ('وجهين ', 'وجهين '),
    )
    print_face = models.CharField(
        max_length=255, null=True, blank=True, choices=PRINT_FACES)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    number_of_pages = models.IntegerField(null=True, blank=True)
    number_of_colors = models.IntegerField(null=True, blank=True)
    number_of_copies = models.IntegerField(null=True, blank=True)

    class Meta:
        pass
