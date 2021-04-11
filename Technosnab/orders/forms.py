from django import forms
from .models import Order, Сustomer
from django.core.exceptions import ValidationError


class OrderForm(forms.ModelForm):
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = 'form-control chosen-select'

    class Meta:
        model = Order
        fields = ['customer', 'car', 'worker', 'product', 'quantity', 'adress', 'caption', 'date', 'time',]

        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control chosen-select'}),
            'car': forms.Select(attrs={'class': 'form-control chosen-select'}),
            'worker': forms.Select(attrs={'class': 'form-control chosen-select'}),
            'product': forms.Select(attrs={'class': 'form-control chosen-select'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'adress': forms.TextInput(attrs={'class': 'form-control'}),
            'caption': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'type': 'date',
                                           'class': 'form-control',
                                           }),
            'time': forms.TextInput(attrs={'type': 'time',
                                           'class': 'form-control'}),
        }





    def clean_pr(self):
        new = self.cleaned_data['phone']

        # if Order.objects.filter(phone__iexact=new).count():
        #     raise ValidationError('Номер должны быть уникальным, такой номер уже существует'.format(new))
        # if Order.objects.filter(passport_number__iexact=new).count():
        #     raise ValidationError('Номер должны быть уникальным, такой номер уже существует'.format(new))


        return new


class СustomerForm(forms.ModelForm):
    class Meta:
        model = Сustomer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
             self.fields[field].widget.attrs['class'] = 'form-control'


    def clean_pr(self):
        new = self.cleaned_data['phone']

        if Сustomer.objects.filter(phone__iexact=new).count():
            raise ValidationError('Номер должны быть уникальным, такой номер уже существует'.format(new))



        return new

