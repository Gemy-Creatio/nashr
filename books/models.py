from django.db import models
from ordered_model.models import OrderedModel
from ckeditor.fields import RichTextField
from accounts.models import User


# Create your models here.
class UserProfile(OrderedModel):
    LANGUAGE_CHOICES = (
        ('1_Arabic', 'العربية'),
        ('2_English', 'الأنجليزية'),
        ('3_French', 'الفرنسية'),
        ('4_Spanish', 'الأسبانية')
    )
    FILED_CHOICES = (
        ('كتب عامة', 'كتب عامة'),
        ('إدارة وأعمال', 'إدارة وأعمال'),
        ('أدب وشعر', 'أدب وشعر'),
        ('أطفال', 'أطفال'),
        ('أكاديمية', 'أكاديمية'),
        ('تراجم وسير', 'تراجم وسير'),
        ('طب وصحة', 'طب وصحة'),
        ('تطوير ذات ', 'تطوير ذات '),
        ('قصص وروايات', 'قصص وروايات'),
        ('كتب دينية', 'كتب دينية'),
        ('كتب صوتية', 'كتب صوتية'),

    )

    mother_language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES)
    contact_info = models.CharField(max_length=255, null=True, blank=True)
    field_concern = models.CharField(max_length=255, blank=True, choices=FILED_CHOICES)
    about_you = RichTextField(null=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    study = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact_info

    class Meta:
        pass


class Book(OrderedModel):
    BOOK_LANGUAGE = (
        ('اللغة العربية', 'اللغة العربية'),
        ('اللغة الإنجليزية', 'اللغة الإنجليزية'),
        ('اللغة الفرنسية', 'اللغة الفرنسية'),
        ('اللغة الألمانية', 'اللغة الألمانية'),
        ('اللغة الروسية', 'اللغة الروسية'),
        ('اللغة اليابانية', 'اللغة اليابانية'),
        ('اللغة الصينية', 'اللغة الصينية'),
    )
    PROJECT_TIME = (
        ('شهرين', 'شهرين'),
        ('ثلاث أشهر', 'ثلاث أشهر'),
        ('ستة أشهر', 'ستة أشهر'),
    )
    BOOK_CATEGORY = (
        ('كتب عامة', 'كتب عامة'),
        ('إدارة وأعمال', 'إدارة وأعمال'),
        ('أدب وشعر', 'أدب وشعر'),
        ('أطفال', 'أطفال'),
        ('أكاديمية', 'أكاديمية'),
        ('تراجم وسير', 'تراجم وسير'),
        ('تطوير ذات', 'تطوير ذات'),
        ('طب وصحة', 'طب وصحة'),
        ('قصص وروايات', 'قصص وروايات'),
        ('كتب دينية', 'كتب دينية'),
    )
    is_completed = models.BooleanField(null=True, default=False)
    is_open_download = models.BooleanField(null=True, default=False)
    book_cover = models.ImageField(upload_to='covers/')
    book_address = models.CharField(null=True, blank=True, max_length=250)
    book_language = models.CharField(choices=BOOK_LANGUAGE, blank=True, max_length=200)
    translate_language = models.CharField(choices=BOOK_LANGUAGE, blank=True, max_length=200)
    pages_number = models.IntegerField(null=True, blank=True)
    translator_number = models.SmallIntegerField(null=True, blank=True)
    translator_fees = models.IntegerField(null=True, blank=True)
    project_time = models.CharField(choices=PROJECT_TIME, blank=True, max_length=200)
    book_category = models.CharField(null=True, max_length=255, choices=BOOK_CATEGORY)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        pass

    def __str__(self):
        return self.book_address


class BookContract(OrderedModel):
    BOOLEAN_CHOICES = (
        (True, 'نعم'),
        (False, 'لا')
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contract = models.FileField(upload_to='contract/')
    is_accepted = models.BooleanField(null=True, blank=True, default=False, choices=BOOLEAN_CHOICES)
    is_entered = models.BooleanField(null=True, blank=True, default=False, choices=BOOLEAN_CHOICES)

    class Meta:
        pass

    def __str__(self):
        return self.author_name


class BookVoucher(OrderedModel):
    PAY_CHOICES = (
        ('تم الدفع', 'تم الدفع'),
        ('لم الدفع', 'لم الدفع')
    )
    BOOLEAN_CHOICES = (
        (True, 'نعم'),
        (False, 'لا')
    )
    contract = models.ForeignKey(BookContract, null=True, on_delete=models.CASCADE)
    first_pay = models.CharField(max_length=255, choices=PAY_CHOICES, null=True)
    second_pay = models.CharField(max_length=255, choices=PAY_CHOICES, null=True)
    third_pay = models.CharField(max_length=255, choices=PAY_CHOICES, null=True)
    first_received = models.DateField(null=True)
    second_received = models.DateField(null=True)
    third_received = models.DateField(null=True)
    is_completed = models.BooleanField(null=True, choices=BOOLEAN_CHOICES)
    is_sent = models.BooleanField(null=True, choices=BOOLEAN_CHOICES)

    class Meta:
        pass

    def __str__(self):
        return self.contract.author_name


class ContractFollow(OrderedModel):
    contract = models.ForeignKey(BookContract, on_delete=models.CASCADE)
    date_added = models.DateField(null=True)
    follow = models.CharField(null=True, max_length=200)
    notes = RichTextField(null=True)

    class Meta:
        pass

    def __str__(self):
        return self.contract.author_name
