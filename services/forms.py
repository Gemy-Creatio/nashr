from django import forms
from services.models import (
    TranslateService,
    SubtitleService ,
    RequestBook
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



class RequestBookForm(forms.ModelForm):
    class Meta:
        model = RequestBook
        exclude = ('user', 'is_shown' , 'data_sent')
        labels = {
            'publisher_name':'اسم دار النشر',
            'book_name':'اسم الكتاب',
            'author_name':'اسم المؤلف ',
            'year_published':' سنة الأصدار ',
            'reason':'سبب اختيار الكتاب ',
            'translator_cv':'السيرة الذاتية',
        }

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
