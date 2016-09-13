__author__ = 'zschweinfurth'

from django.views.generic import TemplateView


class BaseView(TemplateView):

    template_name = 'base/base_page.html'

    def get_context_data(self, **kwargs):

        context = super(BaseView, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        return super(BaseView, self).get(self, request, *args, **kwargs)