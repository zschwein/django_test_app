__author__ = 'zschweinfurth'
from test_app.class_based_views.base.base_view import BaseView


class TestView(BaseView):
    template_name = 'base/base_page.html'

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        return context