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
    number_of_pages = models.IntegerField(null=True, blank=True)
    number_of_colors = models.IntegerField(null=True, blank=True)
    number_of_copies = models.IntegerField(null=True, blank=True)
    book = models.FileField(upload_to='books_print/' , null=True , blank=True)
    class Meta:
        pass




class BookFormating(OrderedModel):
    book_size = models.CharField(max_length=255 , null=True , blank=True)
    book_color = models.CharField(max_length=255 , null=True , blank=True)
    font_type = models.CharField(max_length=255 , null=True , blank=True)
    font_size = models.CharField(max_length=255 , null=True , blank=True)
    drafts = models.CharField(max_length=255 , null=True , blank=True)
    main_address = models.CharField(max_length=255 , null=True , blank=True)
    main_font_type = models.CharField(max_length=255 , null=True , blank=True)
    main_font_size = models.CharField(max_length=255 , null=True , blank=True)
    main_font_color = models.CharField(max_length=255 , null=True , blank=True)
    double_address = models.CharField(max_length=255 , null=True , blank=True)
    sub_address = models.CharField(max_length=255 , null=True , blank=True)
    sub_font_type = models.CharField(max_length=255 , null=True , blank=True)
    sub_font_size = models.CharField(max_length=255 , null=True , blank=True)
    sub_font_color = models.CharField(max_length=255 , null=True , blank=True)
    book_intro = models.CharField(max_length=255 , null=True , blank=True)
    ehda_page = models.CharField(max_length=255 , null=True , blank=True)
    thank_page = models.CharField(max_length=255 , null=True , blank=True)
    define_page = models.CharField(max_length=255 , null=True , blank=True)
    intro_page = models.CharField(max_length=255 , null=True , blank=True)
    book_file = models.FileField(upload_to='format-book/' , null=True , blank=True)
    notes = models.TextField(null=True , blank=True)
    class Meta:
        pass

