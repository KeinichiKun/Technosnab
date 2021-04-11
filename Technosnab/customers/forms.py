from django import forms
from .models import Сustomer
from django.core.exceptions import ValidationError


class СustomerForm(forms.ModelForm):
    class Meta:
        model = Сustomer
        fields = ['phone', 'adres', 'first_name', 'middle_name', 'last_name', 'organization', 'T_customer', 'inn', 'kpp', 'bank', 'rs', 'bik', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
             self.fields[field].widget.attrs['class'] = 'form-control'


    def clean_pr(self):
        new = self.cleaned_data['phone']

        if Сustomer.objects.filter(phone__iexact=new).count():
            raise ValidationError('Номер должны быть уникальным, такой номер уже существует'.format(new))



        return new
