from django import forms
from services.models import (
    TranslateService,
    SubtitleService
)
from django.utils.translation import get_language


def label():
    if get_language() == 'ar':
        return {
            'language': 'اللغة',
            'translate_to': 'النص الهدف',
            'filed': 'مجال النص ',
            'finish_hours': 'الانتهاء من العمل',
            'number_of_pages': 'عدد الصفحات',
            'text_file': 'تحميل النص',

        }
    else:
        return {
            'language': 'Language',
            'translate_to': 'Translate To',
            'filed': 'Text Field',
            'finish_hours': 'Hours To finish',
            'number_of_pages': 'Number Of Pages',
            'text_file': 'Text file',

        }


class TrnaslateServiceForm(forms.ModelForm):
    class Meta:
        model = TranslateService
        exclude = ('user',)
        labels = label()


class SubttileServiceForm(forms.ModelForm):
    class Meta:
        model = SubtitleService
        exclude = ('user',)
        labels = {
            'subtitle_type':'نوع الترجمة',
            'language': 'اللغة',
            'translate_to': 'النص الهدف',
            'filed': 'مجال الفيديو ',
            'finish_hours': 'الانتهاء من العمل',
            'number_of_pages': 'عدد الصفحات',
            'text_file': 'تحميل الفيديو',
            'video_url': 'رابط الفيديو'

        }
