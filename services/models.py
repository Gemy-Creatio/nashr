from django.db import models
from accounts.models import (
    User
)
from ordered_model.models import OrderedModel
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Vouchers(OrderedModel):
    PAID_CHOICES = (
        (True , 'تم الدفع'),
        (False , 'لم يتم الدفع '),
        
    )
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , related_name='paid_vouchers')
    amount = models.IntegerField(null=True , blank=True)
    description = models.TextField(null=True , blank=True)
    get_paid =  models.ForeignKey(User , on_delete=models.SET_NULL , null=True , blank=True , related_name="Paid")
    is_paid = models.BooleanField(null=True , blank=True , default=False,choices=PAID_CHOICES)
    class Meta:
        pass


class PaidVoucher(OrderedModel):
    voucher =  models.ForeignKey(Vouchers , on_delete=models.SET_NULL , null=True)
    date = models.DateField(auto_now_add=True)
    class Meta:
            pass

class TranslateService(OrderedModel):
    text_file = models.FileField(_("Text File"), max_length=255, null=True, blank=True)
    LANGUAGE_CHOICES = (
        ('اللغة العربية', 'اللغة العربية'),
        ('اللغة الإنجليزية', 'اللغة الإنجليزية'),
    )
    language = models.CharField(_("Language"), max_length=255, choices=LANGUAGE_CHOICES, null=True, blank=True)
    number_of_pages = models.IntegerField(_("Number of pages"), null=True, blank=True)
    FILED_CHOICES = (
        ('مجال عام', 'مجال عام'),
        ('مجال سياسي', 'مجال سياسي'),
        ('مجال اقتصادي', 'مجال اقتصادي'),
        ('مجال أكاديمي', 'مجال أكاديمي'),
        ('مجال ديني', 'مجال ديني'),
    )
    filed = models.CharField(_("Field"), max_length=255, choices=FILED_CHOICES, null=True, blank=True)
    TRANSLATE_CHOICES = (
        ('عربي – انجليزي', 'عربي – انجليزي'),
        ('انجليزي - عربي', 'انجليزي - عربي')
    )

    translate_to = models.CharField(_("Translate to"), max_length=255, choices=TRANSLATE_CHOICES, null=True, blank=True)
    FINSIHHOUR_CHOICES = (
        ('ساعة', 'ساعة'),
        ('اربع ساعات', 'اربع ساعات'),

    )
    finish_hours = models.CharField(_("Time to finish"), max_length=255, choices=FINSIHHOUR_CHOICES, null=True,
                                    blank=True)

    class Meta:
        pass


class RequestDesignService(OrderedModel):
    book_size = models.CharField(max_length=255, null=True, blank=True)
    title_book = models.CharField(max_length=255, null=True, blank=True)
    author_name = models.CharField(max_length=255, null=True, blank=True)
    translator_name = models.CharField(max_length=255, null=True, blank=True)
    scientific_rank = models.CharField(max_length=255, null=True, blank=True)
    part_number = models.CharField(max_length=255, null=True, blank=True)
    version_number = models.CharField(max_length=255, null=True, blank=True)
    house_logo = models.CharField(max_length=255, null=True, blank=True)
    about_book = RichTextField(null=True, blank=True)
    isbn_number = models.CharField(max_length=255, null=True, blank=True)
    house_info = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    communication = models.EmailField(max_length=255, null=True, blank=True)
    images = models.ImageField(null=True, blank=True)
    note = RichTextField(null=True, blank=True)
    author_name_tail = models.CharField(max_length=255, null=True, blank=True)
    translator_name_tail = models.CharField(max_length=255, null=True, blank=True)
    scientific_rank_tail = models.CharField(max_length=255, null=True, blank=True)
    part_number_tail = models.CharField(max_length=255, null=True, blank=True)
    version_number_tail = models.CharField(max_length=255, null=True, blank=True)
    is_shown_designer = models.BooleanField(null=True, blank=True, default=False)

    class Meta:
        pass


class RequestProofReader(OrderedModel):
    about_book = RichTextField(null=True, blank=True)
    user_requested = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_shown = models.BooleanField(null=True, blank=True, default=False)

    class Meta:
        pass




