from django.contrib import admin
from budget.models.ExpenseType import ExpenseType
from budget.models.Expenditure import Expenditure

# Register your models here.
admin.site.register(Expenditure)
admin.site.register(ExpenseType)