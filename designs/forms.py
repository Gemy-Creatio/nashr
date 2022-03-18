from django import forms
from designs.models import (
    TakeDesign,
    PrintBookRequest
)


class PrintBookForm(forms.ModelForm):
    class Meta:
        model = PrintBookRequest
        fields = '__all__'
        # labels = {
        #     # 'book': 'الكتاب',
        #     # 'number_of_pages': 'عدد الصفحات',
        #     # 'number_of_colors': 'عدد الألوان',
        #     # 'number_of_copies': 'عدد النسخ',
        # }


class TakeDesignForm(forms.ModelForm):
    class Meta:
        model = TakeDesign
        fields = '__all__'
        labels = {
            'what_designer_introduce': 'ما سيقدم للعميل',
            'max_price': 'السعر الأقصى',
            'min_price': 'السعر الأدنى',
        }
        exclude = ('user',)
