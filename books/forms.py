from django import forms
from .models import (
    UserProfile,
    Book,
    PublisherNeeds

)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ('user',)
        labels = {
            'about_you': 'نبذه عنك ',
            'contact_info': 'رقم التواصل',
            'city': 'المدينة',
            'source': 'النص المصدر',
            'study': 'مؤهلك التعليمي',
            'mother_language': 'اللغة الأم',
            'field_concern': 'مجال الاهتمام',
            'creaditCard_number':'رقم الحساب ',
            'bank_name':'اسم البنك'

        }


class PublisherNeedsForm(forms.ModelForm):
    class Meta:
        model = PublisherNeeds
        exclude = ('publisher', 'is_accepted')
        labels = {
            'needs': 'الوظيفة',
            'name': 'الأسم الثلاثى',
            'email': 'البريد الألكترونى',
            'duration': 'مدة الأنتهاء من العمل',
            'price': 'التكلفة',
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ('user', 'is_completed', 'is_open_download', 'dropbox_link' , 'is_shown')
        labels = {
            'book_content':'محتوى الكتاب',
            'book_address':'عنوان الكتاب',
            'book_language':'لغة الكتاب',
            'translate_language':'لغة الترجمة',
            'pages_number':'عدد الصفح',
            'translator_fees':'أجرة المترجم',
            'book_category':'تصنيف الكتاب',
            'project_time':'وقت الأنتهاء',
            'pay_chocies':'نوعية الدفع',
            'translator_number':'عدد صفح الترجمة',
        }
