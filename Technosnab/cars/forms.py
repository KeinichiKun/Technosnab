from django import forms
from .models import Cars, Expenses
from django.core.exceptions import ValidationError

'''ФОРМА МАШИН'''
class CarFormCreate(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
             self.fields[field].widget.attrs['class'] = 'form-control'


    def clean_pr(self):
        new = self.cleaned_data['state_number']

        if Cars.objects.filter(state_number__iexact=new).count():
            raise ValidationError('Номер должны быть уникальным, такой номер уже существует'.format(new))

        return new


class CarFormEdit(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
             self.fields[field].widget.attrs['class'] = 'form-control'





'''ФОРМА ЗАТРАТ'''
class ExpensesFormCreate(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
             self.fields[field].widget.attrs['class'] = 'form-control'


    def clean_pr(self):
        new = self.cleaned_data['description']

        # if Cars.objects.filter(sdescription__iexact=new).count():
        #    #raise ValidationError('Номер должны быть уникальным, такой номер уже существует'.format(new))

        return new
