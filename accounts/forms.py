from django import forms
from .models import User

USER_TYPES = (
    (2, 'دار نشر'),
    (3, 'مترجم'),

)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_type', 'first_name', 'last_name', 'phone', 'password', 'email', 'address']
        widgets = {
            'user_type': forms.Select(choices=USER_TYPES)
        }
        labels = {
            'user_type': 'هل انت مترجم؟',
            'email': 'البريد الألكترونى',
            'first_name': 'الأسم',
            'last_name': 'اللقب',
            'phone': 'الهاتف',
            'password': 'كلمة المرور',
            'address': 'العنوان',
        }
