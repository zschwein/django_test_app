__author__ = 'zschweinfurth'
from django import forms
from django.forms import ModelForm
from budget.models.ExpenseType import ExpenseType
from budget.models.Expenditure import Expenditure


class ExpenditureForm(ModelForm):

    class Meta:
        model = Expenditure
        fields = ['Date', 'Amount', 'For', 'ExpenseTypeTags']
        widgets = {'Date': forms.DateInput(attrs={'class': 'datepicker'})}

    def clean(self):
        cleaned_data = super(ExpenditureForm, self).clean()

        return cleaned_data