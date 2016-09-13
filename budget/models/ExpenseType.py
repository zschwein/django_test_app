__author__ = 'zschweinfurth'
from django.db import models


class ExpenseType(models.Model):

    class Meta:
        db_table = 'ExpenseType'
        managed = True
        app_label = 'budget'

    ExpenseTypeSk = models.AutoField(primary_key=True)
    ExpenseTypeName = models.CharField(null=False, blank=False, max_length=100, verbose_name='Expense Type')

    def __unicode__(self):
        return self.ExpenseTypeName