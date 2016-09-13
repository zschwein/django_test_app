__author__ = 'zschweinfurth'
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required


from budget.views.class_based_views.test.test_view import TestView
from budget.views.class_based_views.expenditure.expenditure_view import ExpenditureView
from budget.views.functional_views.views import exp_from
from budget.views.functional_views.expenditure_json.expenditure_json import return_exp_json

urlpatterns = [
    url(r'^$', login_required(ExpenditureView.as_view(), ), name='exp'),
    url(r'exp_form$', exp_from, name='exp_form'),
    url(r'get_exp$', return_exp_json, name='return_exp_json'),
]

