from django import forms
from .models import Worker, Position
from django.core.exceptions import ValidationError


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['first_name', 'middle_name', 'last_name', 'P_position', 'passport_seria', 'passport_number', 'passport_issued',
                  'passport_date', 'adress',   ]


        widgets = {
            'passport_date': forms.TextInput(attrs={'type': 'date'})

            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
             self.fields[field].widget.attrs['class'] = 'form-control'


    def clean_pr(self):
        new = self.cleaned_data['phone']

        if Worker.objects.filter(phone__iexact=new).count():
            raise ValidationError('Телефон должны быть уникальным, такой номер уже существует'.format(new))
        # if Worker.objects.filter(passport_number__iexact=new).count():
        #     raise ValidationError('Номер должны быть уникальным, такой номер уже существует'.format(new))


        return new


class PosFormCreate(forms.ModelForm):
    class Meta:
        model = Position
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
             self.fields[field].widget.attrs['class'] = 'form-control'


