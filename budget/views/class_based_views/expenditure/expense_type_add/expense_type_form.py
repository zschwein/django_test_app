__author__ = 'zschweinfurth'
from django.forms import ModelForm
from budget.models.ExpenseType import ExpenseType


class ExpenseTypeForm(ModelForm):

    class Meta:
        model = ExpenseType
        fields = ['ExpenseTypeName']

    def clean(self):
        cleaned_data = super(ExpenseTypeForm, self).clean()

        return cleaned_data