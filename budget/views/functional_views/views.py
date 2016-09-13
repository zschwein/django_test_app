from django.http import HttpResponse

from budget.views.class_based_views.expenditure.expense_type_add.expense_type_form import ExpenseTypeForm


def exp_from(request):
    form = ExpenseTypeForm()
    return HttpResponse(form)