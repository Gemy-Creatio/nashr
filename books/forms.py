from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ('user',)
        labels = {
            'about_you':'نبذه عنك ',
            'contact_info':'رقم التواصل',
            'city': 'المدينة',
            'source': 'النص المصدر',
            'study': 'مؤهلك التعليمي',
            'mother_language': 'اللغة الأم',
            'field_concern': 'مجال الاهتمام',

        }
