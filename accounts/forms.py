from django import forms
from .models import User

USER_TYPES = (
    (2, 'دار نشر'),
    (3, 'مترجم'),
    (4, 'مدقق لغوي'),
    (5, 'مصمم'),
)


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'type:':'email'}), label="البريد الألكترونى")
    password = forms.CharField(widget=forms.TextInput(attrs={'type:':'password'}), label="كلمة المرور")



class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_type', 'first_name', 'last_name', 'phone', 'password', 'email', 'address']
        widgets = {
            'password': forms.TextInput(attrs={'type': 'password'})
        }
        labels = {
            'user_type': 'هل انت ؟',
            'email': 'البريد الألكترونى',
            'first_name': 'الأسم',
            'last_name': 'اللقب',
            'phone': 'الهاتف',
            'password': 'كلمة المرور',
            'address': 'العنوان',
        }

        def __init__(self, *args, **kwargs):
            super(RegisterForm, self).__init__(*args, **kwargs)
            self.fields['user_type'].help_texts = None
