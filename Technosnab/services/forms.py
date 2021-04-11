from django import forms
from .models import Product
from django.core.exceptions import ValidationError
#
# class ServiceForm(forms.Form):
#     class Meta:
#         model = Product
#         fields = '__all__'
#
#
#     def clean_pr(self):
#         new = self.cleaned_data['product_caption']
#
#         # if Product.objects.filter(state_number__iexact=new).count():
#         #     raise ValidationError('Номер должны быть уникальным, такой номер уже существует'.format(new))
#
#         return new
#
#
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields:
#              self.fields[field].widget.attrs['class'] = 'form-control'


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
             self.fields[field].widget.attrs['class'] = 'form-control'


    def clean_pr(self):
        new = self.cleaned_data['product_caption']

        # if Product.objects.filter(state_number__iexact=new).count():
        #     raise ValidationError('Номер должны быть уникальным, такой номер уже существует'.format(new))

        return new

