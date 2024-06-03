from django import forms
from .models import *
class App_Form(forms.ModelForm):
    class Meta:
        model=App
        fields = "__all__"
        widgets = {
        'Name':forms.TextInput(attrs={'placeholder':"Enter App Name"}),
        'URL':forms.TextInput(attrs={'placeholder':'Enter URL'}),
        'price':forms.NumberInput(attrs={'placeholder':'Enter Price'})
        }

        def __init__(self,*args,**kwargs):
            self.instance = kwargs.get('instance', None)
            super().__init__(*args,**kwargs)

        def clean_name(self):
           name = self.cleaned_data.get('name')
           if self.instance:
            # If editing, allow the instance's own name
             if App.objects.filter(name=name).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('This name already exists.')
           else:
             if App.objects.filter(name=name).exists():
                raise forms.ValidationError('This name already exists.')
             return name

        # def clean_name(self):
        #     name=self.cleaned_data.get('name')
        #     if App.objects.filter(name=name).exists():
        #         raise forms.ValidationError("This User already exists")
        #     return name
