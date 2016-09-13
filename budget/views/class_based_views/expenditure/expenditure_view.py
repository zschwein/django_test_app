__author__ = 'zschweinfurth'

import json

from django.http import HttpResponse

from test_app.class_based_views.base.base_view import BaseView
from budget.models.ExpenseType import ExpenseType
from budget.views.class_based_views.expenditure.expenditure_form import ExpenditureForm
from budget.utility.functions import form_id_dic, parse_json_serialized_list, create_full_table_context
from budget.models.Expenditure import Expenditure
from budget.views.class_based_views.expenditure.expense_type_add.expense_type_form import ExpenseTypeForm


class ExpenditureView(BaseView):

    template_name = 'expenditure/expenditure_page.html'
    form_class = ExpenditureForm
    expense_type_form = ExpenseTypeForm
    expense_summary_table_meta = {
            'name': 'test_table',
            'columns': [
                {'col': 'Date',             'label': 'Date',         'filter': 'test_filter'},
                {'col': 'Amount',           'label': 'Amount',       'filter': 'test_filter'},
                {'col': 'For',              'label': 'For',         'filter': 'test_filter'},
                {'col': 'ExpenseTypeTags__ExpenseTypeName',
                 'label': 'Expense Type',
                 'filter': 'test_filter'},
                ]
    }

    def get_context_data(self, **kwargs):
        context = super(ExpenditureView, self).get_context_data(**kwargs)
        context['expense_type_tags'] = self.get_expense_type_tags()

        # call empty form and give it an id
        context['expenditure_form'] = form_id_dic(self.form_class(auto_id=True), 'expenditure_table')
        context['expense_table'] = self.get_user_expenditures()
        context['test_table'] = create_full_table_context(self.expense_summary_table_meta)
        context['expense_type_form'] = self.expense_type_form()
        return context

    def get_expense_type_tags(self):
        data = ExpenseType.objects.all().order_by('ExpenseTypeName')
        tag_list = [item.ExpenseTypeName for item in data]

        return tag_list

    def get_user_expenditures(self):
        data = Expenditure.objects\
            .filter(UserId=self.request.user)\
            .values('Date', 'Amount', 'For', 'ExpenseTypeTags')

        return data

    def post(self, request, *args, **kwargs):

        post_user = request.user

        request_data_recs = parse_json_serialized_list(request.POST.get('data'))

        bad_recs = []
        for rec in request_data_recs:
            form = self.form_class(rec)
            if form.is_valid():
                form_data = form.cleaned_data
                exp = Expenditure(Date=form_data.get('Date'),
                                  Amount=form_data.get('Amount'),
                                  For=form_data.get('For'),
                                  ExpenseTypeTags=form_data.get('ExpenseTypeTags'),
                                  UserId=post_user)
                exp.save()
            else:
                bad_recs.append(rec)

        return HttpResponse(json.dumps(bad_recs))

    def get(self, request, *args, **kwargs):
        if request.GET.get('exp_json') == 'true':
            data = Expenditure.objects\
                   .filter(UserId=self.request.user)\
                   .values('Amount', 'Date', 'For', 'ExpenseTypeTags__ExpenseTypeName')
            response_data = create_full_table_context(self.expense_summary_table_meta, data)
            return HttpResponse(json.dumps({'data': response_data.get('rows')}))
        else:
            return super(ExpenditureView, self).get(self, request, *args, **kwargs)
