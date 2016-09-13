__author__ = 'zschweinfurth'
from budget.models.Expenditure import Expenditure
from json import dumps
from django.http import HttpResponse


def return_exp_json(request):
    user = request.user
    data = Expenditure.objects\
        .filter(UserId=user)\
        .values_list('Amount', 'Date', 'For', 'ExpenseTypeTags__ExpenseTypeName')
    return HttpResponse(dumps({'data': data}),  content_type="application/json")
