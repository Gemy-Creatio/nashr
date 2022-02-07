from django.db import models
from solo.models import SingletonModel
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


# Create your models here.

class WhoUS(SingletonModel):
    heading_en = models.CharField(max_length=255, null=True, help_text=_('Title for Who Us Page [English]'))
    heading_ar = models.CharField(max_length=255, null=True, help_text=_('Title for Who Us Page [Arabic]'))
    content_en = RichTextField(help_text=_('Content for Who Us Page [English]'), null=True)
    content_ar = RichTextField(help_text=_('Content for Who Us Page [Arabic]'), null=True)
    roaya_heading_en = models.CharField(max_length=255, null=True, help_text=_('Title for Roaya Section [English]'))
    roaya_heading_ar = models.CharField(max_length=255, null=True, help_text=_('Title for Roaya Section [Arabic]'))

    roaya_sub_en = models.CharField(max_length=255, null=True, help_text=_('SubTitle for Roaya Section [English]'))
    roaya_sub_ar = models.CharField(max_length=255, null=True, help_text=_('SubTitle for Roaya Section [Arabic]'))
    roaya_content_ar = RichTextField(help_text=_('Content for Who Us Page [English]'), null=True)
    roaya_content_en = RichTextField(help_text=_('Content for Who Us Page [English]'), null=True)
    goals_heading_en = models.CharField(max_length=255, null=True, help_text=_('Title for goals Section [English]'))
    goals_heading_ar = models.CharField(max_length=255, null=True, help_text=_('Title for goals Section [Arabic]'))
    section_goals_en = RichTextField(null=True, help_text=_('Section for goals Page [English]'))
    section_goals_ar = RichTextField(null=True, help_text=_('Section for goals Page [Arabic]'))

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
    heading_ar = models.CharField(max_length=255, null=True, blank=True, help_text=_('Heading for Home Page [Arabic]'))
    heading_en = models.CharField(max_length=255, null=True, blank=True, help_text=_('Heading for Home Page [English]'))
    sub_heading_ar = RichTextField(null=True, help_text=_('sub Heading for Home Page [Arabic]'))
    sub_heading_en = RichTextField(null=True, help_text=_('sub Heading for Home Page [English]'))
    services_heading_ar = models.CharField(max_length=255, null=True, blank=True,
                                           help_text=_('Heading for Service Section Home Page [Arabic]'))
    services_heading_en = models.CharField(max_length=255, null=True, blank=True,
                                           help_text=_('Heading for Service Section Page [English]'))
    services_sub_heading_ar = RichTextField(null=True, help_text=_('sub Heading for Services Home Page [Arabic]'))
    services_sub_heading_en = RichTextField(null=True, help_text=_('sub Heading for Services Home Page [English]'))
    first_section_Service_title_ar = models.CharField(max_length=255, null=True, blank=True,
                                                      help_text=_('title For Service for Home Page [Arabic]'))
    first_sub_heading_ar = RichTextField(null=True, help_text=_('sub Heading for service section [Arabic]'))
    first_services_logo = models.ImageField(upload_to='logos/', null=True)
    second_section_Service_title_ar = models.CharField(max_length=255, null=True, blank=True,
                                                       help_text=_('title For Service for Home Page [Arabic]'))
    second_sub_heading_ar = RichTextField(null=True, help_text=_('sub Heading for service section [Arabic]'))
    second_services_logo = models.ImageField(upload_to='logos/', null=True)
    third_section_Service_title_ar = models.CharField(max_length=255, null=True, blank=True,
                                                      help_text=_('title For Service for Home Page [Arabic]'))
    third_sub_heading_ar = RichTextField(null=True, help_text=_('sub Heading for service section [Arabic]'))
    third_services_logo = models.ImageField(upload_to='logos/', null=True)
    fourth_section_Service_title_ar = models.CharField(max_length=255, null=True, blank=True,
                                                       help_text=_('title For Service for Home Page [Arabic]'))
    fourth_sub_heading_ar = RichTextField(null=True, help_text=_('sub Heading for service section [Arabic]'))
    fourth_services_logo = models.ImageField(upload_to='logos/', null=True)
    substraction_heading_ar = models.CharField(max_length=255, null=True, blank=True,
                                               help_text=_('Substraction Heading for Home Page [Arabic]'))
    substraction_heading_ar = models.CharField(max_length=255, null=True, blank=True,
                                               help_text=_('substraction Heading for Home Page [English]'))
    sub_subsraction_ar = RichTextField(null=True, help_text=_('sub Heading for Home Page [Arabic]'))
    sub_subsraction_en = RichTextField(null=True, help_text=_('sub Heading for Home Page [English]'))

    first_section_Service_title_en = models.CharField(max_length=255, null=True, blank=True,
                                                      help_text=_('title For Service for Home Page [Arabic]'))
    first_sub_heading_en = RichTextField(null=True, help_text=_('sub Heading for service section [Arabic]'))
    second_section_Service_title_en = models.CharField(max_length=255, null=True, blank=True,
                                                       help_text=_('title For Service for Home Page [Arabic]'))
    second_sub_heading_en = RichTextField(null=True, help_text=_('sub Heading for service section [Arabic]'))
    third_section_Service_title_en = models.CharField(max_length=255, null=True, blank=True,
                                                      help_text=_('title For Service for Home Page [Arabic]'))
    third_sub_heading_en = RichTextField(null=True, help_text=_('sub Heading for service section [Arabic]'))
    fourth_section_Service_title_en = models.CharField(max_length=255, null=True, blank=True,
                                                       help_text=_('title For Service for Home Page [Arabic]'))
    fourth_sub_heading_en = RichTextField(null=True, help_text=_('sub Heading for service section [Arabic]'))

    substraction_heading_en = models.CharField(max_length=255, null=True, blank=True,
                                               help_text=_('title For Substraction for Home Page [English]'))

    substraction_logo = models.ImageField(upload_to='logos/', null=True)
    class Meta:
        pass
