from django import forms
from designs.models import (
    TakeDesign
)


class TakeDesignForm(forms.ModelForm):
    class Meta:
        model = TakeDesign
        fields = '__all__'
        labels = {
            'what_designer_introduce': 'ما سيقدم للعميل',
            'max_price': 'السعر الأقصى',
            'min_price': 'السعر الأدنى',
        }
        exclude = ('user' , )
