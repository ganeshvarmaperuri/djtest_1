from django import forms
from .models import EmpModelForm

class EmpForm(forms.ModelForm):
    class Meta:
        model = EmpModelForm
        fields = '__all__'


