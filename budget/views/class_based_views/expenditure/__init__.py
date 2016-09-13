__author__ = 'zschweinfurth'

from test_app.class_based_views.base.base_view import BaseView


class ExpenditureView(BaseView):

    template_name = 'expenditure/expenditure_page.html'


    def get_context_data(self, **kwargs):
        context = super(ExpenditureView, self).get_context_data(**kwargs)
        return context