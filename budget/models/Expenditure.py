__author__ = 'zschweinfurth'
from django.db import models
from budget.models.ExpenseType import ExpenseType
from django.contrib.auth.models import User


class Expenditure(models.Model):

    class Meta:
        db_table = 'Expendiutre'
        managed = True
        app_label = 'budget'

    ExpenditureSk = models.AutoField(primary_key=True)
    Date = models.DateTimeField(verbose_name='Expenditure Date', null=False, blank=False)
    Amount = models.DecimalField(verbose_name='Expenditure Amount', max_digits=14, decimal_places=2,
                                 null=False, blank=False)
    For = models.CharField(verbose_name='Expenditure For', null=False, blank=False, max_length=100)
    ExpenseTypeTags = models.ForeignKey(ExpenseType, related_name='Expense', blank=True, null=True)
    UserId = models.ForeignKey(User, db_column='UserId', related_name='Expense', blank=False, null=False)
