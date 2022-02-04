from django.db import models
from solo.models import SingletonModel
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


# Create your models here.

class WhoUS(SingletonModel):
    heading_en = models.CharField(max_length=255, null=True, help_text=_('Title for Who Us Page [English]'))
    heading_ar = models.CharField(max_length=255, null=True, help_text=_('Title for Who Us Page [Arabic]'))
    content_en = RichTextField(help_text=_('Content for Who Us Page [English]'))
    content_ar = RichTextField(help_text=_('Content for Who Us Page [Arabic]'))

    class Meta:
        pass


class Privacy(SingletonModel):
    heading_en = models.CharField(max_length=255, null=True, help_text=_('Title for Privacy Page [English]'))
    heading_ar = models.CharField(max_length=255, null=True, help_text=_('Title for Privacy Page [Arabic]'))
    sub_heading_en = models.CharField(max_length=255, null=True, help_text=_('SubTitle for Privacy Page [English]'))
    sub_heading_ar = models.CharField(max_length=255, null=True, help_text=_('SubTitle for Privacy Page [Arabic]'))
    section_one_en = RichTextField(null=True, help_text=_('Section one for Privacy Page [English]'))
    section_one_ar = RichTextField(null=True, help_text=_('Section one for Privacy Page [Arabic]'))
    section_two_en = RichTextField(null=True, help_text=_('Section two for Privacy Page [English]'))
    section_two_ar = RichTextField(null=True, help_text=_('Section two for Privacy Page [Arabic]'))
    section_three_en = RichTextField(null=True, help_text=_('Section three for Privacy Page [English]'))
    section_three_ar = RichTextField(null=True, help_text=_('Section three for Privacy Page [Arabic]'))
    section_four_en = RichTextField(null=True, help_text=_('Section four for Privacy Page [English]'))
    section_four_ar = RichTextField(null=True, help_text=_('Section four for Privacy Page [Arabic]'))
    section_five_en = RichTextField(null=True, help_text=_('Section five for Privacy Page [English]'))
    section_five_ar = RichTextField(null=True, help_text=_('Section five for Privacy Page [Arabic]'))
    section_six_en = RichTextField(null=True, help_text=_('Section six for Privacy Page [English]'))
    section_six_ar = RichTextField(null=True, help_text=_('Section six for Privacy Page [Arabic]'))
    section_seven_en = RichTextField(null=True, help_text=_('Section seven for Privacy Page [English]'))
    section_seven_ar = RichTextField(null=True, help_text=_('Section seven for Privacy Page [Arabic]'))

    class Meta:
        pass


class About(SingletonModel):
    roaya_heading_en = models.CharField(max_length=255, null=True, help_text=_('Title for Roaya Section [English]'))
    roaya_heading_ar = models.CharField(max_length=255, null=True, help_text=_('Title for Roaya Section [Arabic]'))
    roaya_sub_en = models.CharField(max_length=255, null=True, help_text=_('SubTitle for Roaya Section [English]'))
    roaya_sub_ar = models.CharField(max_length=255, null=True, help_text=_('SubTitle for Roaya Section [Arabic]'))
    section_roaya_en = RichTextField(null=True, help_text=_('Section for Roaya Page [English]'))
    section_roaya_ar = RichTextField(null=True, help_text=_('Section for Roaya Page [Arabic]'))
    goals_heading_en = models.CharField(max_length=255, null=True, help_text=_('Title for goals Section [English]'))
    goals_heading_ar = models.CharField(max_length=255, null=True, help_text=_('Title for goals Section [Arabic]'))
    goals_sub_en = models.CharField(max_length=255, null=True, help_text=_('SubTitle for goals Section [English]'))
    goals_sub_ar = models.CharField(max_length=255, null=True, help_text=_('SubTitle for goals Section [Arabic]'))
    section_goals_en = RichTextField(null=True, help_text=_('Section for goals Page [English]'))
    section_goals_ar = RichTextField(null=True, help_text=_('Section for goals Page [Arabic]'))
    roles_heading_en = models.CharField(max_length=255, null=True, help_text=_('Title for roles Section [English]'))
    roles_heading_ar = models.CharField(max_length=255, null=True, help_text=_('Title for roles Section [Arabic]'))
    roles_sub_en = models.CharField(max_length=255, null=True, help_text=_('SubTitle for roles Section [English]'))
    roles_sub_ar = models.CharField(max_length=255, null=True, help_text=_('SubTitle for roles Section [Arabic]'))
    section_roles_en = RichTextField(null=True, help_text=_('Section for roles Page [English]'))
    section_roles_ar = RichTextField(null=True, help_text=_('Section for roles Page [Arabic]'))

    class Meta:
        pass


class MembershipTerms(SingletonModel):
    heading_en = models.CharField(max_length=255, null=True, help_text=_('Title for MemberShipTerms Page [English]'))
    heading_ar = models.CharField(max_length=255, null=True, help_text=_('Title for MemberShipTerms Page [Arabic]'))
    sub_heading_en = models.CharField(max_length=255, null=True,
                                      help_text=_('SubTitle for MemberShipTerms Page [English]'))
    sub_heading_ar = models.CharField(max_length=255, null=True,
                                      help_text=_('SubTitle for MemberShipTerms Page [Arabic]'))
    section_one_en = RichTextField(null=True, help_text=_('Section one for MemberShipTerms Page [English]'))
    section_one_ar = RichTextField(null=True, help_text=_('Section one for MemberShipTerms Page [Arabic]'))
    section_two_en = RichTextField(null=True, help_text=_('Section two for MemberShipTerms Page [English]'))
    section_two_ar = RichTextField(null=True, help_text=_('Section two for MemberShipTerms Page [Arabic]'))
    section_three_en = RichTextField(null=True, help_text=_('Section three for MemberShipTerms Page [English]'))
    section_three_ar = RichTextField(null=True, help_text=_('Section three for MemberShipTerms Page [Arabic]'))
    section_four_en = RichTextField(null=True, help_text=_('Section four for MemberShipTerms Page [English]'))
    section_four_ar = RichTextField(null=True, help_text=_('Section four for MemberShipTerms Page [Arabic]'))
    section_five_en = RichTextField(null=True, help_text=_('Section five for MemberShipTerms Page [English]'))
    section_five_ar = RichTextField(null=True, help_text=_('Section five for MemberShipTerms Page [Arabic]'))
    section_six_en = RichTextField(null=True, help_text=_('Section six for MemberShipTerms Page [English]'))
    section_six_ar = RichTextField(null=True, help_text=_('Section six for MemberShipTerms Page [Arabic]'))
    section_seven_en = RichTextField(null=True, help_text=_('Section seven for MemberShipTerms Page [English]'))
    section_seven_ar = RichTextField(null=True, help_text=_('Section seven for MemberShipTerms Page [Arabic]'))

    class Meta:
        pass


class Homepage(SingletonModel):
    what_we_offer_en = models.CharField(max_length=255, null=True,
                                        help_text=_('Title for What we offers section [English]'))
    what_we_offer_ar = models.CharField(max_length=255, null=True,
                                        help_text=_('Title for What we offers section  [Arabic]'))
    what_we_offer_sub_en = models.CharField(max_length=255, null=True,
                                            help_text=_('Subitle for What we offers section [English]'))
    what_we_offer_sub_ar = models.CharField(max_length=255, null=True,
                                            help_text=_('Subitle for What we offers section  [Arabic]'))
    what_we_offer_btn_txt_en = models.CharField(max_length=255, null=True,
                                                help_text=_('text for button in What we offers section [English]'))
    what_we_offer_btn_txt_ar = models.CharField(max_length=255, null=True,
                                                help_text=_('text for button in What we offers section [Arabic]'))
    SERVICES_CHOICES_AR = (
        ('تصميم الغلاف', 'تصميم الغلاف'),
        ('تنسيق الكتاب', 'تنسيق الكتاب'),
        ('السترجة', 'السترجة'),
        ('النسخ الصوتى', 'النسخ الصوتى'),
    )
    SERVICES_CHOICES_EN = (
        ('Cover design', 'Cover design'),
        ('Book format', 'Book format'),
        ('Subtraction', 'Subtraction'),
        ('Audio transcription', 'Audio transcription'),
    )
    service_one_title_en = models.CharField(max_length=255, null=True,
                                            help_text=_('Title for Services section [English]'),
                                            choices=SERVICES_CHOICES_EN)
    service_one_title_ar = models.CharField(max_length=255, null=True,
                                            help_text=_('Title for Services section  [Arabic]'),
                                            choices=SERVICES_CHOICES_AR)
    service_one_summary_en = RichTextField(null=True,
                                           help_text=_('Summary Services section [English]'))
    service_one_summary_ar = RichTextField(null=True,
                                           help_text=_('Summary for Services section  [Arabic]'))
    service_two_title_en = models.CharField(max_length=255, null=True,
                                            help_text=_('Title for Services section [English]'),
                                            choices=SERVICES_CHOICES_EN)
    service_two_title_ar = models.CharField(max_length=255, null=True,
                                            help_text=_('Title for Services section  [Arabic]'),
                                            choices=SERVICES_CHOICES_AR)
    service_two_summary_en = RichTextField(null=True,
                                           help_text=_('Summary Services section [English]'))
    service_two_summary_ar = RichTextField(null=True,
                                           help_text=_('Summary for Services section  [Arabic]'))
    service_three_title_en = models.CharField(max_length=255, null=True,
                                              help_text=_('Title for Services section [English]'),
                                              choices=SERVICES_CHOICES_EN)
    service_three_title_ar = models.CharField(max_length=255, null=True,
                                              help_text=_('Title for Services section  [Arabic]'),
                                              choices=SERVICES_CHOICES_AR)
    service_three_summary_en = RichTextField(null=True,
                                             help_text=_('Summary Services section [English]'))
    service_three_summary_ar = RichTextField(null=True,
                                             help_text=_('Summary for Services section  [Arabic]'))
    service_four_title_en = models.CharField(max_length=255, null=True,
                                             help_text=_('Title for Services section [English]'),
                                             choices=SERVICES_CHOICES_EN)
    service_four_title_ar = models.CharField(max_length=255, null=True,
                                             help_text=_('Title for Services section  [Arabic]'),
                                             choices=SERVICES_CHOICES_AR)
    service_four_summary_en = RichTextField(null=True,
                                            help_text=_('Summary Services section [English]'))
    service_four_summary_ar = RichTextField(null=True,
                                            help_text=_('Summary for Services section  [Arabic]'))
    contact_title_en = models.CharField(max_length=255, null=True,
                                        help_text=_('Title for Contact section [English]'))
    address_en = RichTextField(null=True,
                               help_text=_('Address Contact section [English]'))
    contact_title_ar = models.CharField(max_length=255, null=True,
                                        help_text=_('Title for Contact section [Arabic]'))
    address_ar = RichTextField(null=True,
                               help_text=_('Address Contact section [Arabic]'))
    phone_nashr = models.CharField(max_length=255, null=True,
                                   help_text=_('Phone Number for Contact section [Arabic]'))

    def last_projects(self):
        from books.models import Book
        books = Book.objects.filter(is_completed=True)[:4]
        return books
